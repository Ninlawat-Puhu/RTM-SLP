from torch import nn, Tensor
import torch
import torch.nn as nn

class RtmLoss(nn.Module):
    """
    RTM Loss: Shape-Corrected MSE based on Hanson Correlation (PyTorch Version)
    """

    def __init__(self, eps=1e-8):
        super(RtmLoss, self).__init__()
        """
        Initialize the metric calculator.
        eps: Small value to prevent division by zero.
        """
        self.eps = eps
        
        # Attributes for analysis/debugging
        self.rho = None            # Complex correlation (Shape + Rotation)
        self.mag_rho = None        # Magnitude of correlation (Shape similarity 0-1)
        self.scale_ratio = None    # b (std_tgt / std_pred)
        self.factor = None         # Factor used for regression (b * |rho|)
        self.diff_vector = None    # Residual vector (x, y) after correction

    def forward(self, pred_data, tgt_data):

        vt_pred = pred_data 
        vt_tgt  = tgt_data

        mean_pred = torch.mean(vt_pred, dim=1, keepdim=True)
        mean_tgt  = torch.mean(vt_tgt,  dim=1, keepdim=True)

        vc_pred = vt_pred - mean_pred
        vc_tgt  = vt_tgt  - mean_tgt

        std_pred = torch.sqrt(torch.mean(torch.sum(vc_pred**2, dim=2), dim=1))
        std_tgt  = torch.sqrt(torch.mean(torch.sum(vc_tgt**2,  dim=2), dim=1))

        z = torch.complex(vc_pred[..., 0], vc_pred[..., 1])
        w = torch.complex(vc_tgt[..., 0],  vc_tgt[..., 1])

        sigma_zw = torch.mean(z * torch.conj(w), dim=1)
        denom = std_pred * std_tgt
        
        self.rho = torch.zeros_like(sigma_zw)
        
        valid_mask = denom > self.eps
        self.rho[valid_mask] = sigma_zw[valid_mask] / denom[valid_mask]

        self.mag_rho = torch.abs(self.rho)

        self.scale_ratio = std_tgt / (std_pred + self.eps)

        self.factor = (self.scale_ratio * self.mag_rho).reshape(-1, 1, 1)

        damped_factor = self.factor

        self.diff_vector = vc_tgt - (damped_factor * vc_pred)

        squared_error_per_joint = torch.sum(self.diff_vector**2, dim=2) 

        mse_per_frame = torch.mean(squared_error_per_joint, dim=1)

        total_mse = torch.mean(mse_per_frame)
        
        return total_mse