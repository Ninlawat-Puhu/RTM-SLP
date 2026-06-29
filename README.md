# Mitigating Regression-to-the-Mean Effects in Pose-Based Autoregressive Sign Language Production

## Abstract
Sign Language Production (SLP) aims to generate sign language representations from spoken-language inputs. Autoregressive SLP models suffer from regression-to-the-mean (RTM) effects, where continuous keypoint prediction produces over-smoothed motions, reducing sign expressiveness. Accumulated prediction errors can degrade long-term motion consistency. This paper proposes an autoregressive Transformer framework for text-to-sign and gloss-to-sign generation. To improve the quality of generated sign motions, the framework introduces three components. First, we propose an RTM loss function designed to preserve temporal variations in sign keypoint sequences and mitigate motion over-smoothing. Second, a recursive keypoint reasoning module is introduced to refine generated motion representations and enhance keypoint accuracy. Third, a large language model-based linguistic prosody prediction module is integrated to estimate gloss-level intensity information for conditional sign generation. The proposed method is evaluated on PHOENIX14T, How2Sign, and mDGS using back-translation metrics and pose-quality metrics, including Dynamic Time Warping Mean Joint Error, Fréchet Gesture Distance (FGD), and Mean Absolute Error of Joint Coordinates (MAEJ). On the PHOENIX14T text-to-sign test set, the proposed model reduces FGD from 43.477 for the strongest evaluated baseline to 0.500, corresponding to a 98.8% reduction, and reduces MAEJ error from 0.0716 to 0.0121. For gloss-to-sign generation on PHOENIX14T, the full intensity-conditioned configuration achieves an FGD of 0.198 and MAEJ of 0.0100, whereas removing intensity conditioning yields a higher back-translation BLEU-4 score of 6.27. Similar pose-quality improvements are observed on How2Sign and mDGS, demonstrating the generalization ability of the proposed framework, although back-translation performance gains remain dataset-dependent.

## Demo
We provide qualitative demonstrations of the generated sign pose sequences produced by the proposed framework. Each visualization contains two synchronized skeleton sequences for direct comparison between the generated output and the reference motion.

- **Left skeleton:** Ground-truth pose sequence extracted from the original sign language video.
- **Right skeleton:** Generated pose sequence predicted by our proposed method.

The demonstrations are organized into two sign language production configuration:

- **Text-to-Sign (T2S):** generating sign pose sequences directly from spoken language inputs.
- **Gloss-to-Sign (G2S):** generating sign pose sequences from gloss-level sign representations with intensity information.

### Text-to-Sign (T2S) Examples

### RWTH-PHOENIX-Weather-2014T

![](Videos/T2S/phoenix/t2s_phoenix_1.gif)

![](Videos/T2S/phoenix/t2s_phoenix_2.gif)

![](Videos/T2S/phoenix/t2s_phoenix_3.gif)

### Meine DGS Annotated

![](Videos/T2S/mdgs/t2s_mdgs_1.gif)

![](Videos/T2S/mdgs/t2s_mdgs_2.gif)

![](Videos/T2S/mdgs/t2s_mdgs_3.gif)

### How2Sign

![](Videos/T2S/How2Sign/t2s_h2s_1.gif)

![](Videos/T2S/How2Sign/t2s_h2s_2.gif)

![](Videos/T2S/How2Sign/t2s_h2s_3.gif)

### Gloss-to-Sign (G2S) Examples

### RWTH-PHOENIX-Weather-2014T

![](Videos/G2S/phoenix/g2s_phoenix_1.gif)

![](Videos/G2S/phoenix/g2s_phoenix_2.gif)

![](Videos/G2S/phoenix/g2s_phoenix_3.gif)

### Meine DGS Annotated

![](Videos/G2S/mdgs/g2s_mdgs_1.gif)

![](Videos/G2S/mdgs/g2s_mdgs_2.gif)

![](Videos/G2S/mdgs/g2s_mdgs_3.gif)


### Comparison with Different k Times
Here we also provide qualitative comparisons under different self-reasoning refinement steps ($k$ times)

![](Videos/comparison/t2s_k_steps_phonix_3cols.gif)

![](Videos/comparison/t2s_k_steps_phonix_6cols.gif)

### Comparison to Progressive Transformer
We compare our full approach with the Progressive Transformer baseline optimized with Mean Squared Error (MSE) loss. Our method integrates RTM loss and recursive keypoint to mitigate over-smoothed motions.

![](Videos/comparison/t2s_comparison_rtm_pg_1.gif)

![](Videos/comparison/t2s_comparison_rtm_pg_2.gif)


### Effect of Prosody Conditioning
We compare the generated sign pose sequences with and without the proposed LLM-based prosody conditioning module.

![](Videos/comparison/g2s_phoenix_comparison_prosody_1.gif)

![](Videos/comparison/g2s_phoenix_comparison_prosody_2.gif)

### Failure Case Examples
Across all datasets (RWTH-PHOENIX-Weather-2014T, Meine DGS Annotated, and How2Sign), we observe similar challenging failure patterns. In particular, the generated facial poses may not perfectly align with the ground truth when signers exhibit large head or body movements. Additionally, highly detailed hand configurations can still be challenging in cases involving rapid or complex hand motions.

![](Videos/failure_cases/g2s_mdgs_failcase_1.gif)

![](Videos/failure_cases/g2s_mdgs_failcase_2.gif)

![](Videos/failure_cases/g2s_phoenix_failcase_1.gif)

![](Videos/failure_cases/g2s_phoenix_failcase_2.gif)

![](Videos/failure_cases/t2s_h2s_failcase_1.gif)

![](Videos/failure_cases/t2s_h2s_failcase_2.gif)

