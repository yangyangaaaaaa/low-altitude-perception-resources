# 低空环境感知基座模型研究综述：方法、数据集与论文开放资源

> 面向低空无人机视觉感知与遥感基础模型研究的资源导航。主页直接列出方法、模型、数据集、论文、关键词及可访问入口，便于按任务和研究主题快速查找。

本项目围绕综述涉及的目标检测、语义分割、遥感视觉表征、视觉语言、多模态理解、视频跟踪、无人机导航和三维重建等方向，汇集方法、模型、数据集与论文入口。主页正文直接展示完整资源导航；CSV 文件仅作为便于筛选、排序和二次整理的表格版本。

方法条目集中呈现研究方向、检索关键词、论文题名及论文/代码入口；数据集资料卡补充任务简介、关键词、多个数据或项目入口及相关论文。可先按任务分类浏览，再根据关键词快速定位，并直接打开论文、数据或项目页面。同一篇论文中的模型后缀或配置变体并入一个条目，常见名称直接合并到方法名称中；“—”表示该条目没有对应入口。

如果本清单对你的研究有帮助，欢迎在项目页面 Star，并通过 Issue 或 Pull Request 补充公开资源入口、纠正链接或完善介绍。
## 快速导航

- [资源概况](#资源概况)
- [精选入口](#精选入口)
- [方法与模型](#方法与模型)
  - [目标检测与开放词汇定位](#目标检测与开放词汇定位)
  - [视觉骨干与通用学习方法](#视觉骨干与通用学习方法)
  - [视觉语言与多模态理解](#视觉语言与多模态理解)
  - [视频理解与时序表征](#视频理解与时序表征)
  - [视频目标跟踪与时序感知](#视频目标跟踪与时序感知)
  - [无人机导航与具身智能](#无人机导航与具身智能)
  - [遥感预训练与视觉表征](#遥感预训练与视觉表征)
  - [语义分割与像素级理解](#语义分割与像素级理解)
- [数据集与基准](#数据集与基准)
  - [目标检测、跟踪与航空视觉](#目标检测跟踪与航空视觉)
  - [语义分割与场景理解](#语义分割与场景理解)
  - [多模态与遥感数据](#多模态与遥感数据)
  - [三维重建与多视图](#三维重建与多视图)
  - [无人机导航与具身任务](#无人机导航与具身任务)
- [评价指标与评测代码](#评价指标与评测代码)
- [论文索引](#论文索引)
- [引用与使用说明](#引用与使用说明)
- [文件说明](#文件说明)
## 资源概况

| 类别 | 条目数 | 页面内容 |
| :--- | ---: | :--- |
| 方法与模型 | 142 | 研究方向、关键词、论文题名、论文入口、代码/项目入口及合并名称 |
| 数据集与基准 | 18 | 用途简介、任务关键词、多个数据入口及相关论文 |
| 论文记录 | 159 | 可直接打开的论文题名、主题关键词和链接 |
| 评价指标 | 29 | 指标说明、公开代码/协议入口及本包基础辅助代码 |

## 精选入口

从综述中的核心主题出发，优先列出具有代表性的模型、数据集与导航基准。

| 资源 | 方向 | 关键词 | 论文 | 项目/数据入口 |
| :--- | :--- | :--- | :--- | :--- |
| RingMo-Aerial | 方法/模型 | 遥感视觉；预训练表征；遥感影像；对比表征 | [RingMo-Aerial: An Aerial Remote Sensing Foundation Model With Affine Transformation Contrastive Learning](https://doi.org/10.1109/TPAMI.2025.3602237) | — |
| Text2Earth | 方法/模型 | 视觉语言；多模态理解；遥感影像；图像生成 | [Text2Earth: Unlocking Text-driven Remote Sensing Image Generation with a Global-Scale Dataset and a Foundation Model](https://doi.org/10.1109/MGRS.2025.3560455) | [项目说明/代码](https://github.com/Chen-Yang-Liu/Text2Earth) |
| Grounding DINO | 方法/模型 | 目标检测；开放词汇/开放集；自监督/掩码预训练 | [Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection](https://arxiv.org/abs/2303.05499) | [项目说明/代码](https://github.com/IDEA-Research/GroundingDINO) |
| DINOv2 | 方法/模型 | 视觉表征；预训练与迁移 | [DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193) | [项目说明/代码](https://github.com/facebookresearch/dinov2) |
| AI-TOD | 数据集/基准 | AI-TOD；小目标；航空影像；检测；密集目标 | [A Normalized Gaussian Wasserstein Distance for Tiny Object Detection](https://arxiv.org/abs/2110.13389) | [项目说明/代码](https://github.com/jwwangchn/AI-TOD) |
| WHU-MVS / WHU-OMVS | 数据集/基准 | WHU-OMVS；多视图立体；斜视航空影像；深度估计；三维重建 | [Deep learning based multi-view stereo matching and 3D scene reconstruction from oblique aerial images](https://doi.org/10.1016/j.isprsjprs.2023.08.015) | [数据主页](https://gpcv.whu.edu.cn/data/WHU_OMVS_dataset/WHU_dataset.htm)<br>[项目说明/代码](https://github.com/gpcv-liujin/Ada-MVS)<br>[数据主页](https://gpcv.whu.edu.cn/data/) |
| UDD6 | 数据集/基准 | 无人机；城市场景；语义分割；立面；道路；植被；车辆；屋顶；其他 | [Large-Scale Structure From Motion With Semantic Constraints of Aerial Images](https://doi.org/10.1007/978-3-030-03398-9_30) | [项目说明/代码](https://github.com/MarcWong/UDD)<br>[Google Drive 数据](https://drive.google.com/file/d/1BNL8HNFRiNjSzdcQJo-uXiejZJ6DgunY/view?usp=sharing)<br>[百度网盘数据](https://pan.baidu.com/s/1sQavCwH29PUwTEgF3teMBQ) |
| VisDrone | 数据集/基准 | 无人机视觉；检测；跟踪 | [VisDrone-DET2021: The Vision Meets Drone Object Detection in Image and Video](https://doi.org/10.1109/ICCVW54120.2021.00319) | [项目说明/代码](https://github.com/VisDrone/VisDrone-Dataset)<br>[VisDrone 资源主页](https://aiskyeye.com/) |
| TravelUAV | 数据集/基准 | 无人机；视觉语言导航；仿真平台；TRAVEL；数据集 | [Towards Realistic UAV Vision-Language Navigation: Platform, Benchmark, and Methodology](https://arxiv.org/abs/2410.07087) | [项目说明/代码](https://github.com/buaa-colalab/TravelUAV)<br>[OpenUAV 项目主页](https://prince687028.github.io/OpenUAV/)<br>[Hugging Face 数据集](https://huggingface.co/datasets/wangxiangyu0814/TravelUAV) |
| OpenFly / AerialVLN | 数据集/基准 | 视觉语言导航；无人机；具身智能；轨迹 | [Openfly: A comprehensive platform for aerial vision-language navigation](https://arxiv.org/abs/2502.18041) | [OpenFly 项目主页](https://shailab-ipec.github.io/openfly/) |

## 方法与模型

按研究方向浏览方法、模型和代表性论文。关键词便于快速定位技术路线；论文题名可直接打开论文页面，代码/项目列链接到公开仓库或项目主页。

### 目标检测与开放词汇定位

涵盖通用目标检测、无人机航拍检测、开放词汇识别与小目标定位。

| 方法/模型 | 关键词 | 论文 | 代码/项目 |
| :--- | :--- | :--- | :--- |
| DDQ-DETR | 目标检测；Transformer | [Dense Distinct Query for End-to-End Object Detection](https://arxiv.org/abs/2303.12776) | [项目说明/代码](https://github.com/jshilong/DDQ) |
| Detic | 目标检测 | [Detecting Twenty-thousand Classes using Image-level Supervision](https://arxiv.org/abs/2201.02605) | [项目说明/代码](https://github.com/facebookresearch/Detic) |
| DETR | 目标检测；Transformer | [End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872) | [项目说明/代码](https://github.com/facebookresearch/detr) |
| DINO | 目标检测；Transformer | [DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection](https://arxiv.org/abs/2203.03605) | [项目说明/代码](https://github.com/IDEA-Research/DINO) |
| FBRT-YOLO / FBRT-YOLO-X | 目标检测；航空小目标；实时/高效；遥感影像 | [FBRT-YOLO: Faster and Better for Real-Time Aerial Image Detection](https://doi.org/10.1609/aaai.v39i8.32937) | — |
| Grounding DINO | 目标检测；开放词汇/开放集；自监督/掩码预训练 | [Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection](https://arxiv.org/abs/2303.05499) | [项目说明/代码](https://github.com/IDEA-Research/GroundingDINO) |
| OGMN | 目标检测；航空小目标；遮挡鲁棒 | [OGMN: Occlusion-guided Multi-task Network for Object Detection in UAV Images](https://arxiv.org/abs/2304.11805) | — |
| OWL-ViT | 目标检测；开放词汇/开放集；Transformer | [Simple Open-Vocabulary Object Detection with Vision Transformers](https://arxiv.org/abs/2205.06230) | [项目说明/代码](https://github.com/google-research/scenic) |
| OWLv2 | 目标检测；开放词汇/开放集 | [Scaling Open-Vocabulary Object Detection](https://arxiv.org/abs/2306.09683) | [项目说明/代码](https://github.com/google-research/scenic) |
| RetinaNet | 目标检测 | [Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002) | [项目说明/代码](https://github.com/facebookresearch/detectron2) |
| SPAR | 目标检测；提示学习 | [Self-Prompting Analogical Reasoning for UAV Object Detection](https://doi.org/10.1609/aaai.v39i17.34026) | — |
| UAV-DETR / UAV-DETR-R50 | 目标检测；实时/高效；Transformer；遥感影像 | [UAV-DETR: Efficient End-to-End Object Detection for Unmanned Aerial Vehicle Imagery](https://doi.org/10.1109/IROS60139.2025.11246176) | [项目说明/代码](https://github.com/ValiantDiligent/UAV-DETR) |

### 视觉骨干与通用学习方法

汇集视觉与语言基础表征、预训练、自监督学习和通用特征学习工作。

| 方法/模型 | 关键词 | 论文 | 代码/项目 |
| :--- | :--- | :--- | :--- |
| ALBEF | 视觉表征；预训练与迁移；对比表征 | [Align before Fuse: Vision and Language Representation Learning with Momentum Distillation](https://arxiv.org/abs/2107.07651) | [项目说明/代码](https://github.com/salesforce/ALBEF) |
| Baichuan | 视觉表征；预训练与迁移 | [Baichuan 2: Open Large-scale Language Models](https://arxiv.org/abs/2309.10305) | [项目说明/代码](https://github.com/baichuan-inc/Baichuan2) |
| BART | 视觉表征；预训练与迁移；自监督/掩码预训练；图像生成 | [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461) | [项目主页](https://research.facebook.com/publications/bart-denoising-sequence-to-sequence-pre-training-for-natural-language-generation-translation-and-comprehension/) |
| BYOL | 视觉表征；预训练与迁移；自监督/掩码预训练 | [Bootstrap your own latent: A new approach to self-supervised Learning](https://arxiv.org/abs/2006.07733) | [项目说明/代码](https://github.com/Spijkervet/BYOL) |
| Chameleon | 视觉表征；预训练与迁移；多模态/跨模态 | [Chameleon: Mixed-Modal Early-Fusion Foundation Models](https://arxiv.org/abs/2405.09818) | [项目说明/代码](https://github.com/facebookresearch/chameleon) |
| CoCa | 视觉表征；预训练与迁移；视觉语言；对比表征 | [CoCa: Contrastive Captioners are Image-Text Foundation Models](https://arxiv.org/abs/2205.01917) | [项目说明/代码](https://github.com/lucidrains/coca-pytorch) |
| ConSERT | 视觉表征；预训练与迁移；自监督/掩码预训练；对比表征 | [ConSERT: A Contrastive Framework for Self-Supervised Sentence Representation Transfer](https://arxiv.org/abs/2105.11741) | [项目说明/代码](https://github.com/kg-nlp/ConSERT) |
| CSP | 视觉表征；预训练与迁移；自监督/掩码预训练；对比表征 | [CSP: Self-Supervised Contrastive Spatial Pre-Training for Geospatial-Visual Representations](https://arxiv.org/abs/2305.01118) | [项目说明/代码](https://github.com/gengchenmai/csp) |
| DeepSeek | 视觉表征；预训练与迁移；实时/高效 | [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) | [项目说明/代码](https://github.com/deepseek-ai/DeepSeek-LLM) |
| DiffCSE | 视觉表征；预训练与迁移；对比表征 | [DiffCSE: Difference-based Contrastive Learning for Sentence Embeddings](https://arxiv.org/abs/2204.10298) | [项目说明/代码](https://github.com/voidism/diffcse) |
| DINOv2 | 视觉表征；预训练与迁移 | [DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193) | [项目说明/代码](https://github.com/facebookresearch/dinov2) |
| DRCI | 视觉表征；预训练与迁移；实时/高效；目标跟踪；对比表征 | [Towards Discriminative Representations with Contrastive Instances for Real-Time UAV Tracking](https://arxiv.org/abs/2308.11450) | — |
| DualToken | 视觉表征；预训练与迁移；图像生成 | [DualToken: Towards Unifying Visual Understanding and Generation with Dual Visual Vocabularies](https://arxiv.org/abs/2503.14324) | [项目说明/代码](https://github.com/songweii/DualToken) |
| ELECTRA | 视觉表征；预训练与迁移；自监督/掩码预训练 | [ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators](https://arxiv.org/abs/2003.10555) | [项目说明/代码](https://github.com/google-research/electra) |
| Falcon | 视觉表征；预训练与迁移；视觉语言；遥感影像 | [Falcon: A Remote Sensing Vision-Language Foundation Model (Technical Report)](https://arxiv.org/abs/2503.11070) | [项目说明/代码](https://github.com/TianHuiLab/Falcon) |
| FILIP | 视觉表征；预训练与迁移；视觉语言；自监督/掩码预训练 | [FILIP: Fine-grained Interactive Language-Image Pre-Training](https://arxiv.org/abs/2111.07783) | — |
| FLIP | 视觉表征；预训练与迁移；视觉语言；自监督/掩码预训练 | [Scaling Language-Image Pre-training via Masking](https://arxiv.org/abs/2212.00794) | [项目说明/代码](https://github.com/facebookresearch/flip) |
| GeoPixel | 视觉表征；预训练与迁移；多模态/跨模态；遥感影像 | [GeoPixel: Pixel Grounding Large Multimodal Model in Remote Sensing](https://arxiv.org/abs/2501.13925) | [项目说明/代码](https://github.com/mbzuai-oryx/GeoPixel) |
| GLIP | 视觉表征；预训练与迁移；视觉语言；自监督/掩码预训练 | [Grounded Language-Image Pre-training](https://arxiv.org/abs/2112.03857) | [项目说明/代码](https://github.com/microsoft/GLIP) |
| HYDRA | 视觉表征；预训练与迁移；智能体/具身任务 | [HYDRA: A Hyper Agent for Dynamic Compositional Visual Reasoning](https://link.springer.com/chapter/10.1007/978-3-031-72661-3_8) | [项目说明/代码](https://github.com/ControlNet/HYDRA) |
| InternLM / InternLM2 | 视觉表征；预训练与迁移 | [InternLM2 Technical Report](https://arxiv.org/abs/2403.17297) | [项目说明/代码](https://github.com/InternLM/InternLM) |
| K-Lite | 视觉表征；预训练与迁移 | [K-LITE: Learning Transferable Visual Models with External Knowledge](https://arxiv.org/abs/2204.09222) | [项目说明/代码](https://github.com/microsoft/klite) |
| LiT | 视觉表征；预训练与迁移；开放词汇/开放集；视觉语言 | [LiT: Zero-Shot Transfer with Locked-image text Tuning](https://arxiv.org/abs/2111.07991) | [项目说明/代码](https://github.com/google-research/vision_transformer) |
| LLaMA | 视觉表征；预训练与迁移；实时/高效 | [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) | [项目说明/代码](https://github.com/meta-llama/llama) |
| LXMERT | 视觉表征；预训练与迁移；Transformer；多模态/跨模态；对比表征 | [LXMERT: Learning Cross-Modality Encoder Representations from Transformers](https://arxiv.org/abs/1908.07490) | [项目说明/代码](https://github.com/airsplay/lxmert) |
| MA3E | 视觉表征；预训练与迁移；自监督/掩码预训练；遥感影像 | [Masked Angle-Aware Autoencoder for Remote Sensing Images](https://arxiv.org/abs/2408.01946) | [项目说明/代码](https://github.com/benesakitam/MA3E) |
| MASS | 视觉表征；预训练与迁移；自监督/掩码预训练；图像生成 | [MASS: Masked Sequence to Sequence Pre-training for Language Generation](https://arxiv.org/abs/1905.02450) | [项目说明/代码](https://github.com/microsoft/MASS) |
| Megatron-LM | 视觉表征；预训练与迁移 | [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053) | [项目说明/代码](https://github.com/NVIDIA/Megatron-LM) |
| Mini-Gemini | 视觉表征；预训练与迁移；视觉语言；多模态/跨模态 | [Mini-Gemini: Mining the Potential of Multi-modality Vision Language Models](https://arxiv.org/abs/2403.18814) | [项目说明/代码](https://github.com/JIA-Lab-research/MGM) |
| MM-Interleaved | 视觉表征；预训练与迁移；视觉语言；多模态/跨模态；图像生成 | [MM-Interleaved: Interleaved Image-Text Generative Modeling via Multi-modal Feature Synchronizer](https://arxiv.org/abs/2401.10208) | [项目说明/代码](https://github.com/OpenGVLab/MM-Interleaved) |
| MSN | 视觉表征；预训练与迁移；实时/高效；自监督/掩码预训练 | [Masked Siamese Networks for Label-Efficient Learning](https://arxiv.org/abs/2204.07141) | [项目说明/代码](https://github.com/facebookresearch/msn) |
| OSCAR | 视觉表征；预训练与迁移；视觉语言；自监督/掩码预训练 | [Oscar: Object-Semantics Aligned Pre-training for Vision-Language Tasks](https://arxiv.org/abs/2004.06165) | [论文/资料页](https://arxiv.org/abs/2004.06165) |
| RACF | 视觉表征；预训练与迁移；实时/高效；目标跟踪 | [Learning residue-aware correlation filters and refining scale for real-time UAV tracking](https://doi.org/10.1016/j.patcog.2022.108614) | — |
| SARATR-X | 视觉表征；预训练与迁移；SAR影像 | [SARATR-X: Toward Building A Foundation Model for SAR Target Recognition](https://arxiv.org/abs/2405.09365) | [项目说明/代码](https://github.com/waterdisappear/SARATR-X) |
| SDST | 视觉表征；预训练与迁移；Transformer；自监督/掩码预训练；高光谱 | [SDST: Self-Supervised Double-Structure Transformer for Hyperspectral Images Clustering](https://ieeexplore.ieee.org/document/10462168) | — |
| SwAV | 视觉表征；预训练与迁移；自监督/掩码预训练 | [Unsupervised Learning of Visual Features by Contrasting Cluster Assignments](https://arxiv.org/abs/2006.09882) | [项目说明/代码](https://github.com/facebookresearch/swav) |
| UniLM | 视觉表征；预训练与迁移；自监督/掩码预训练；图像生成 | [Unified Language Model Pre-training for Natural Language Understanding and Generation](https://arxiv.org/abs/1905.03197) | [项目说明/代码](https://github.com/microsoft/unilm) |
| UNIMO | 视觉表征；预训练与迁移；多模态/跨模态；图像生成；对比表征 | [UNIMO: Towards Unified-Modal Understanding and Generation via Cross-Modal Contrastive Learning](https://arxiv.org/abs/2012.15409) | [项目说明/代码](https://github.com/PaddlePaddle/Research/tree/master/NLP/UNIMO) |
| UNIT | 视觉表征；预训练与迁移 | [UNIT: Unifying Image and Text Recognition in One Vision Encoder](https://arxiv.org/abs/2409.04095) | [项目说明/代码](https://github.com/yeezhu/UNIT) |
| UNITER | 视觉表征；预训练与迁移；视觉语言；对比表征 | [UNITER: UNiversal Image-TExt Representation Learning](https://arxiv.org/abs/1909.11740) | [项目说明/代码](https://github.com/ChenRocks/UNITER) |
| VQGAN | 视觉表征；预训练与迁移；Transformer；图像生成 | [Taming Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2012.09841) | [项目说明/代码](https://github.com/CompVis/taming-transformers) |
| XLM | 视觉表征；预训练与迁移；自监督/掩码预训练 | [Cross-lingual Language Model Pretraining](https://arxiv.org/abs/1901.07291) | [项目说明/代码](https://github.com/facebookresearch/XLM) |
| XLNet | 视觉表征；预训练与迁移；自监督/掩码预训练 | [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237) | [项目说明/代码](https://github.com/zihangdai/xlnet) |

### 视觉语言与多模态理解

包括图文对齐、视觉问答、多模态生成、遥感视觉语言模型及跨模态理解。

| 方法/模型 | 关键词 | 论文 | 代码/项目 |
| :--- | :--- | :--- | :--- |
| ALBERT | 视觉语言；多模态理解；自监督/掩码预训练；对比表征 | [ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/abs/1909.11942) | [项目说明/代码](https://github.com/google-research/albert) |
| ALIGN | 视觉语言；多模态理解；对比表征 | [Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision](https://arxiv.org/abs/2102.05918) | — |
| BERT | 视觉语言；多模态理解；Transformer；自监督/掩码预训练 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | [项目说明/代码](https://github.com/google-research/bert) |
| BLIP | 视觉语言；多模态理解；自监督/掩码预训练；图像生成 | [BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](https://arxiv.org/abs/2201.12086) | [项目说明/代码](https://github.com/salesforce/BLIP) |
| BLIP-2 | 视觉语言；多模态理解；自监督/掩码预训练 | [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597) | [项目说明/代码](https://github.com/salesforce/LAVIS) |
| CLIP | 视觉语言；多模态理解 | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | [项目说明/代码](https://github.com/openai/CLIP) |
| CogVLM | 视觉语言；多模态理解 | [CogVLM: Visual Expert for Pretrained Language Models](https://arxiv.org/abs/2311.03079) | [项目说明/代码](https://github.com/THUDM/CogVLM) |
| DeBERTa | 视觉语言；多模态理解 | [DeBERTa: Decoding-enhanced BERT with Disentangled Attention](https://arxiv.org/abs/2006.03654) | [项目说明/代码](https://github.com/microsoft/DeBERTa) |
| DeepSeek-VL | 视觉语言；多模态理解 | [DeepSeek-VL: Towards Real-World Vision-Language Understanding](https://arxiv.org/abs/2403.05525) | [项目说明/代码](https://github.com/deepseek-ai/DeepSeek-VL) |
| DGTRS-CLIP | 视觉语言；多模态理解；遥感影像 | [DGTRSD & DGTRS-CLIP: A Dual-Granularity Remote Sensing Image-Text Dataset and Vision Language Foundation Model for Alignment](https://arxiv.org/abs/2503.19311) | [项目说明/代码](https://github.com/MitsuiChen14/DGTRS) |
| DOFA-CLIP | 视觉语言；多模态理解；多模态/跨模态 | [DOFA-CLIP: Multimodal Vision-Language Foundation Models for Earth Observation](https://arxiv.org/abs/2503.06312) | [项目说明/代码](https://github.com/zhu-xlab/DOFA) |
| EarthGPT | 视觉语言；多模态理解；多模态/跨模态；遥感影像 | [EarthGPT: A Universal Multimodal Large Language Model for Multisensor Image Comprehension in Remote Sensing Domain](https://doi.org/10.1109/TGRS.2024.3409624) | [项目说明/代码](https://github.com/wivizhang/EarthGPT) |
| EarthGPT-X | 视觉语言；多模态理解；遥感影像；提示学习 | [EarthGPT-X: A Spatial MLLM for Multilevel Multisource Remote Sensing Imagery Understanding With Visual Prompting](https://doi.org/10.1109/TGRS.2025.3626941) | — |
| FLAVA | 视觉语言；多模态理解 | [FLAVA: A Foundational Language And Vision Alignment Model](https://arxiv.org/abs/2112.04482) | — |
| GeoChat | 视觉语言；多模态理解；遥感影像 | [GeoChat: Grounded Large Vision-Language Model for Remote Sensing](https://arxiv.org/abs/2311.15826) | [项目说明/代码](https://github.com/mbzuai-oryx/GeoChat) |
| GeoCLIP | 视觉语言；多模态理解 | [GeoCLIP: Clip-Inspired Alignment between Locations and Images for Effective Worldwide Geo-localization](https://arxiv.org/abs/2309.16020v2) | [项目说明/代码](https://github.com/VicenteVivan/geo-clip) |
| GLM | 视觉语言；多模态理解 | [GLM-130B: An Open Bilingual Pre-trained Model](https://arxiv.org/abs/2210.02414) | [项目说明/代码](https://github.com/THUDM/GLM) |
| GPT | 视觉语言；多模态理解；自监督/掩码预训练；图像生成 | [Improving Language Understanding by Generative Pre-Training](https://www.mikecaptain.com/resources/pdf/GPT-1.pdf) | [项目说明/代码](https://github.com/openai/gpt-2) |
| iGPT | 视觉语言；多模态理解；自监督/掩码预训练；图像生成 | [Generative Pretraining from Pixels](https://cdn.openai.com/papers/Generative_Pretraining_from_Pixels_V2.pdf) | [项目说明/代码](https://github.com/openai/image-gpt) |
| ImageBind | 视觉语言；多模态理解 | [ImageBind: One Embedding Space To Bind Them All](https://arxiv.org/abs/2305.05665) | [项目说明/代码](https://github.com/facebookresearch/ImageBind) |
| InternVL | 视觉语言；多模态理解 | [InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks](https://arxiv.org/abs/2312.14238) | [项目说明/代码](https://github.com/OpenGVLab/InternVL) |
| LaCLIP | 视觉语言；多模态理解 | [Improving CLIP Training with Language Rewrites](https://arxiv.org/abs/2305.20088) | [项目说明/代码](https://github.com/lijiefan/laclip) |
| LLaMA-VID | 视觉语言；多模态理解 | [LLaMA-VID: An Image is Worth 2 Tokens in Large Language Models](https://arxiv.org/abs/2311.17043) | [项目说明/代码](https://github.com/dvlab-research/LLaMA-VID) |
| LLaVA | 视觉语言；多模态理解 | [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485) | [项目说明/代码](https://github.com/haotian-liu/LLaVA) |
| LLaVA-1.5 | 视觉语言；多模态理解 | [Improved Baselines with Visual Instruction Tuning](https://arxiv.org/abs/2310.03744) | [项目说明/代码](https://github.com/haotian-liu/LLaVA) |
| LLaVA-CoT | 视觉语言；多模态理解 | [LLaVA-CoT: Let Vision Language Models Reason Step-by-Step](https://arxiv.org/abs/2411.10440) | [项目说明/代码](https://github.com/PKU-YuanGroup/LLaVA-CoT) |
| MoE-LLaVA | 视觉语言；多模态理解 | [MoE-LLaVA: Mixture of Experts for Large Vision-Language Models](https://arxiv.org/abs/2401.15947) | [项目说明/代码](https://github.com/PKU-YuanGroup/MoE-LLaVA) |
| mT5 | 视觉语言；多模态理解；Transformer | [mT5: A massively multilingual pre-trained text-to-text transformer](https://arxiv.org/abs/2010.11934) | [项目说明/代码](https://github.com/google-research/multilingual-t5) |
| Pixel-BERT | 视觉语言；多模态理解；Transformer；多模态/跨模态 | [Pixel-BERT: Aligning Image Pixels with Text by Deep Multi-Modal Transformers](https://arxiv.org/abs/2004.00849) | — |
| PromptBERT | 视觉语言；多模态理解；提示学习 | [PromptBERT: Improving BERT Sentence Embeddings with Prompts](https://arxiv.org/abs/2201.04337) | [项目说明/代码](https://github.com/kongds/Prompt-BERT) |
| Qwen | 视觉语言；多模态理解 | [Qwen Technical Report](https://arxiv.org/abs/2309.16609) | [项目说明/代码](https://github.com/QwenLM/Qwen) |
| Qwen-VL | 视觉语言；多模态理解 | [Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond](https://arxiv.org/abs/2308.12966) | [项目说明/代码](https://github.com/QwenLM/Qwen-VL) |
| RegionCLIP | 视觉语言；多模态理解；自监督/掩码预训练 | [RegionCLIP: Region-based Language-Image Pretraining](https://arxiv.org/abs/2112.09106) | [项目说明/代码](https://github.com/microsoft/RegionCLIP) |
| Remote Sense ChatGPT | 视觉语言；多模态理解；遥感影像 | [Remote Sensing ChatGPT: Solving Remote Sensing Tasks With ChatGPT and Visual Models](https://doi.org/10.1109/IGARSS53475.2024.10640736) | [项目说明/代码](https://github.com/HaonanGuo/Remote-Sensing-ChatGPT) |
| RemoteCLIP | 视觉语言；多模态理解；遥感影像 | [RemoteCLIP: A Vision Language Foundation Model for Remote Sensing](https://arxiv.org/abs/2306.11029) | [项目说明/代码](https://github.com/ChenDelong1999/RemoteCLIP) |
| RoBERTa | 视觉语言；多模态理解；自监督/掩码预训练 | [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692) | [项目说明/代码](https://github.com/facebookresearch/fairseq/tree/main/examples/roberta) |
| SatCLIP | 视觉语言；多模态理解 | [SatCLIP: Global, General-Purpose Location Embeddings with Satellite Imagery](https://arxiv.org/abs/2311.17179) | [项目说明/代码](https://github.com/microsoft/satclip) |
| T5 | 视觉语言；多模态理解；Transformer | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683) | [项目说明/代码](https://github.com/google-research/text-to-text-transfer-transformer) |
| Text2Earth | 视觉语言；多模态理解；遥感影像；图像生成 | [Text2Earth: Unlocking Text-driven Remote Sensing Image Generation with a Global-Scale Dataset and a Foundation Model](https://doi.org/10.1109/MGRS.2025.3560455) | [项目说明/代码](https://github.com/Chen-Yang-Liu/Text2Earth) |
| Tree-GPT | 视觉语言；多模态理解；遥感影像 | [TREE-GPT: Modular Large Language Model Expert System for Forest Remote Sensing Image Understanding and Interactive Analysis](https://doi.org/10.5194/isprs-archives-XLVIII-1-W2-2023-1729-2023) | — |
| Video-ChatGPT | 视觉语言；多模态理解 | [Video-ChatGPT: Towards Detailed Video Understanding via Large Vision and Language Models](https://arxiv.org/abs/2306.05424) | [项目说明/代码](https://github.com/mbzuai-oryx/Video-ChatGPT) |
| VinVL | 视觉语言；多模态理解；对比表征 | [VinVL: Revisiting Visual Representations in Vision-Language Models](https://arxiv.org/abs/2101.00529) | [项目说明/代码](https://github.com/pzzhang/VinVL) |
| VISPROG | 视觉语言；多模态理解 | [Visual Programming: Compositional visual reasoning without training](https://arxiv.org/abs/2211.11559) | [项目说明/代码](https://github.com/allenai/visprog) |
| VLMo | 视觉语言；多模态理解；自监督/掩码预训练 | [VLMo: Unified Vision-Language Pre-Training With Mixture-of-Modality-Experts](https://arxiv.org/abs/2111.02358) | — |
| X-VLM | 视觉语言；多模态理解；自监督/掩码预训练 | [Multi-Grained Vision Language Pre-Training: Aligning Texts with Visual Concepts](https://arxiv.org/abs/2111.08276) | [项目说明/代码](https://github.com/zengyan-97/X-VLM) |

### 视频理解与时序表征

关注视频预训练、长视频理解、掩码建模和连续时序特征表达。

| 方法/模型 | 关键词 | 论文 | 代码/项目 |
| :--- | :--- | :--- | :--- |
| MetaMorph | 视频理解；时序表征；多模态/跨模态；图像生成 | [MetaMorph: Multimodal Understanding and Generation via Instruction Tuning](https://arxiv.org/abs/2412.14164) | [项目说明/代码](https://github.com/facebookresearch/metamorph) |
| VideoMAE | 视频理解；时序表征；实时/高效；自监督/掩码预训练 | [VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training](https://arxiv.org/abs/2203.12602) | [项目说明/代码](https://github.com/MCG-NJU/VideoMAE) |
| VideoMAEv2 | 视频理解；时序表征；自监督/掩码预训练 | [VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking](https://arxiv.org/abs/2303.16727) | [项目说明/代码](https://github.com/OpenGVLab/VideoMAEv2) |
| VideoTree | 视频理解；时序表征；对比表征 | [VideoTree: Adaptive Tree-based Video Representation for LLM Reasoning on Long Videos](https://arxiv.org/abs/2405.19209) | [项目说明/代码](https://github.com/Ziyang412/VideoTree) |

### 视频目标跟踪与时序感知

收录单目标与多目标跟踪、遮挡处理、运动模糊鲁棒性及跨帧关联方法。

| 方法/模型 | 关键词 | 论文 | 代码/项目 |
| :--- | :--- | :--- | :--- |
| Aba-ViTrack | 目标跟踪；跨帧关联；实时/高效；Transformer | [Adaptive and Background-Aware Vision Transformer for Real-Time UAV Tracking](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Adaptive_and_Background-Aware_Vision_Transformer_for_Real-Time_UAV_Tracking_ICCV_2023_paper.pdf) | [项目说明/代码](https://github.com/xyyang317/Aba-ViTrack) |
| AVTrack / AVTrack-DeiT | 目标跟踪；跨帧关联；实时/高效；Transformer | [Learning an Adaptive and View-Invariant Vision Transformer for Real-Time UAV Tracking](https://arxiv.org/abs/2412.20002) | [项目说明/代码](https://github.com/wuyou3474/AVTrack) |
| BDTrack | 目标跟踪；跨帧关联；实时/高效；模糊鲁棒；Transformer | [Learning Motion Blur Robust Vision Transformers for Real-Time UAV Tracking](https://arxiv.org/abs/2407.05383) | [项目说明/代码](https://github.com/wuyou3474/BDTrack) |
| ByteTrack | 目标跟踪；跨帧关联 | [ByteTrack: Multi-Object Tracking by Associating Every Detection Box](https://arxiv.org/abs/2110.06864) | [项目说明/代码](https://github.com/ifzhang/ByteTrack) |
| CenterTrack | 目标跟踪；跨帧关联 | [CenterTrack: Tracking Objects as Points](https://arxiv.org/abs/2004.01177) | [项目说明/代码](https://github.com/xingyizhou/CenterTrack) |
| ORTrack / ORTrack-D-DeiT | 目标跟踪；跨帧关联；实时/高效；遮挡鲁棒；Transformer | [Learning Occlusion-Robust Vision Transformers for Real-Time UAV Tracking](https://arxiv.org/abs/2504.09228) | [项目说明/代码](https://github.com/wuyou3474/ORTrack) |
| SAM-Track | 目标跟踪；跨帧关联 | [Segment and Track Anything](https://arxiv.org/abs/2305.06558) | [项目说明/代码](https://github.com/z-x-yang/Segment-and-Track-Anything) |

### 无人机导航与具身智能

聚焦空中视觉语言导航、环境交互、任务规划和无人机具身决策。

| 方法/模型 | 关键词 | 论文 | 代码/项目 |
| :--- | :--- | :--- | :--- |
| Change-Agent | 无人机导航；具身任务；遥感影像；智能体/具身任务 | [Change-Agent: Towards Interactive Comprehensive Remote Sensing Change Interpretation and Analysis](https://arxiv.org/abs/2403.19646) | [项目说明/代码](https://github.com/Chen-Yang-Liu/Change-Agent) |
| CityNavAgent | 无人机导航；具身任务；遥感影像；视觉导航；智能体/具身任务 | [CityNavAgent: Aerial Vision-and-Language Navigation With Hierarchical Semantic Planning and Global Memory](https://doi.org/10.18653/v1/2025.acl-long.1511) | [项目说明/代码](https://github.com/EmbodiedCity/CityNavAgent.code) |
| FlightGPT | 无人机导航；具身任务；视觉语言；视觉导航 | [FlightGPT: Towards Generalizable and Interpretable UAV Vision-and-Language Navigation With Vision-Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.338) | [项目说明/代码](https://github.com/Uavln/FlightGPT) |
| LongFly | 无人机导航；具身任务；视觉导航 | [LongFly: Long-Horizon UAV Vision-and-Language Navigation with Spatiotemporal Context Integration](https://arxiv.org/abs/2512.22010) | — |
| NavAgent | 无人机导航；具身任务；多模态/跨模态；视觉导航；智能体/具身任务 | [NavAgent: Multi-scale Urban Street View Fusion For UAV Embodied Vision-and-Language Navigation](https://arxiv.org/abs/2411.08579) | — |
| OpenFly-Agent | 无人机导航；具身任务；视觉语言；遥感影像；视觉导航 | [Openfly: A comprehensive platform for aerial vision-language navigation](https://arxiv.org/abs/2502.18041) | [项目说明/代码](https://github.com/SHAILAB-IPEC/OpenFly-Platform) |
| RS-Agent | 无人机导航；具身任务；遥感影像；智能体/具身任务 | [RS-Agent: Automating Remote Sensing Tasks through Intelligent Agent](https://arxiv.org/abs/2406.07089) | [项目说明/代码](https://github.com/intellisensing/rs-agent) |
| UAV-VLN | 无人机导航；具身任务；视觉语言；视觉导航 | [UAV-VLN: End-to-End Vision Language Guided Navigation for UAVs](https://doi.org/10.1109/ECMR65884.2025.11163198) | — |

### 遥感预训练与视觉表征

面向遥感与航空影像的基础模型、自监督预训练、跨模态表征和场景迁移。

| 方法/模型 | 关键词 | 论文 | 代码/项目 |
| :--- | :--- | :--- | :--- |
| BEiT | 遥感视觉；预训练表征；Transformer；自监督/掩码预训练 | [BEiT: BERT Pre-Training of Image Transformers](https://arxiv.org/abs/2106.08254) | — |
| HyperSIGMA | 遥感视觉；预训练表征；高光谱 | [HyperSIGMA: Hyperspectral Intelligence Comprehension Foundation Model](https://arxiv.org/abs/2406.11519) | [项目说明/代码](https://github.com/WHU-Sigma/HyperSIGMA) |
| LeMeViT | 遥感视觉；预训练表征；实时/高效；Transformer；遥感影像 | [LeMeViT: Efficient Vision Transformer with Learnable Meta Tokens for Remote Sensing Image Interpretation](https://arxiv.org/abs/2405.09789) | [项目说明/代码](https://github.com/ViTAE-Transformer/LeMeViT) |
| MAE | 遥感视觉；预训练表征；自监督/掩码预训练 | [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377) | [项目说明/代码](https://github.com/facebookresearch/mae) |
| MAGE | 遥感视觉；预训练表征；自监督/掩码预训练；图像生成；对比表征 | [MAGE: Masked Generative Encoder to Unify Representation Learning and Image Synthesis](https://ieeexplore.ieee.org/document/10203945/) | [项目说明/代码](https://github.com/LTH14/MAGE) |
| MoCo | 遥感视觉；预训练表征；自监督/掩码预训练；对比表征 | [Momentum Contrast for Unsupervised Visual Representation Learning](https://arxiv.org/abs/1911.05722) | [项目说明/代码](https://github.com/facebookresearch/moco) |
| PVT | 遥感视觉；预训练表征；Transformer | [Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions](https://arxiv.org/abs/2102.12122) | [项目说明/代码](https://github.com/whai362/PVT) |
| RingMo-Aerial（C、D、M、U） | 遥感视觉；预训练表征；遥感影像；对比表征 | [RingMo-Aerial: An Aerial Remote Sensing Foundation Model With Affine Transformation Contrastive Learning](https://doi.org/10.1109/TPAMI.2025.3602237) | — |
| RVSA | 遥感视觉；预训练表征；Transformer；遥感影像 | [Advancing Plain Vision Transformer Towards Remote Sensing Foundation Model](https://arxiv.org/abs/2208.03987) | [项目说明/代码](https://github.com/ViTAE-Transformer/Remote-Sensing-RVSA) |
| SatMAE | 遥感视觉；预训练表征；Transformer；自监督/掩码预训练；高光谱 | [SatMAE: Pre-training Transformers for Temporal and Multi-Spectral Satellite Imagery](https://arxiv.org/abs/2207.08051) | [项目说明/代码](https://github.com/sustainlab-group/SatMAE) |
| Scale-MAE | 遥感视觉；预训练表征；自监督/掩码预训练；对比表征 | [Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning](https://arxiv.org/abs/2212.14532) | [项目说明/代码](https://github.com/bair-climate-initiative/scale-mae) |
| SimCLR | 遥感视觉；预训练表征；对比表征 | [A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2002.05709) | [项目说明/代码](https://github.com/google-research/simclr) |
| SimCSE / SupSimCSE | 遥感视觉；预训练表征；对比表征 | [SimCSE: Simple Contrastive Learning of Sentence Embeddings](https://doi.org/10.18653/v1/2021.emnlp-main.552) | — |
| SimMIM | 遥感视觉；预训练表征；自监督/掩码预训练 | [SimMIM: A Simple Framework for Masked Image Modeling](https://arxiv.org/abs/2111.09886) | [项目说明/代码](https://github.com/microsoft/SimMIM) |
| USat | 遥感视觉；预训练表征；自监督/掩码预训练 | [USat: A Unified Self-Supervised Encoder for Multi-Sensor Satellite Imagery](https://arxiv.org/abs/2312.02199) | [项目说明/代码](https://github.com/stanfordmlgroup/USat) |
| ViT | 遥感视觉；预训练表征；Transformer | [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) | [项目说明/代码](https://github.com/google-research/vision_transformer) |

### 语义分割与像素级理解

包括遥感场景语义分割、提示式分割和像素级结构解析方法。

| 方法/模型 | 关键词 | 论文 | 代码/项目 |
| :--- | :--- | :--- | :--- |
| DeepLabV3+ | 图像分割；像素级理解 | [Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1802.02611) | [项目说明/代码](https://github.com/VainF/DeepLabV3Plus-Pytorch) |
| HRNet | 图像分割；像素级理解；对比表征 | [Deep High-Resolution Representation Learning for Visual Recognition](https://arxiv.org/abs/1908.07919) | [项目说明/代码](https://github.com/HRNet/HRNet-Semantic-Segmentation) |
| MaskFeat | 图像分割；像素级理解；自监督/掩码预训练 | [Masked Feature Prediction for Self-Supervised Visual Pre-Training](https://arxiv.org/abs/2112.09133) | [项目说明/代码](https://github.com/facebookresearch/SlowFast/tree/main/projects/maskfeat) |
| MaskGIT | 图像分割；像素级理解；Transformer；自监督/掩码预训练；图像生成 | [MaskGIT: Masked Generative Image Transformer](https://arxiv.org/abs/2202.04200) | [项目说明/代码](https://github.com/google-research/maskgit) |
| RSPrompter | 图像分割；像素级理解；遥感影像；提示学习 | [RSPrompter: Learning to Prompt for Remote Sensing Instance Segmentation based on Visual Foundation Model](https://arxiv.org/abs/2306.16269) | [项目说明/代码](https://github.com/KyanChen/RSPrompter) |
| SAM | 图像分割；像素级理解 | [Segment Anything](https://arxiv.org/abs/2304.02643) | [项目说明/代码](https://github.com/facebookresearch/segment-anything) |
| UAVFormer | 图像分割；像素级理解；航空小目标；Transformer | [UAVformer: A Composite Transformer Network for Urban Scene Segmentation of UAV Images](https://doi.org/10.1016/j.patcog.2022.109019) | — |

## 数据集与基准

每项资源均以资料卡展示任务方向、内容简介、检索关键词、数据或项目入口和相关论文。一个数据集存在多个数据页、项目页或下载镜像时，分别提供入口，读者可以直接选择合适的页面。

### 目标检测、跟踪与航空视觉

#### AerialSARData

**任务方向：** 航空SAR车辆检测

面向航空合成孔径雷达（SAR）车辆检测的影像资源，由六旋翼无人机搭载 MS-102 小型SAR采集；原论文报告711幅800×800影像，其中训练集536幅、测试集175幅，覆盖机场、道路和居民区等场景。

**关键词：** SAR；航空遥感；车辆检测；无人机；RingMo-Aerial

**数据与项目入口：** [论文/资料页](https://arxiv.org/html/2409.13366)

**补充入口：** [论文/资料页](https://arxiv.org/abs/2409.13366)<br>[论文/资料页](https://doi.org/10.1109/TPAMI.2025.3602237)

**相关论文：** [RingMo-Aerial: An Aerial Remote Sensing Foundation Model With Affine Transformation Contrastive Learning](https://doi.org/10.1109/TPAMI.2025.3602237)

#### AI-TOD

**任务方向：** 航空小目标检测

面向航空影像极小目标检测的数据集，官方项目页介绍了28,036幅航空影像、700,621个目标实例和约12.8像素的平均目标尺寸，适合研究密集小目标、尺度变化和检测器召回能力。

**关键词：** AI-TOD；小目标；航空影像；检测；密集目标

**数据与项目入口：** [项目说明/代码](https://github.com/jwwangchn/AI-TOD)

**相关论文：** [A Normalized Gaussian Wasserstein Distance for Tiny Object Detection](https://arxiv.org/abs/2110.13389)

#### AIR-MOT

**任务方向：** 航空视频多目标跟踪

面向卫星视频多目标跟踪的 AIR-MOT 数据集，官方项目页提供已发布的视频下载入口，并给出数据集说明和论文引用信息，适合轨迹建模、图结构跟踪与多任务跟踪研究。

**关键词：** 多目标跟踪；卫星视频；AIR-MOT；图结构

**数据与项目入口：** [项目说明/代码](https://github.com/HeQibin/TGraM)

**补充入口：** [Google Drive 数据](https://drive.google.com/drive/folders/1zfvhKOGmvZVWUgbE8l3LL9ude0bBg-O?usp=sharing)

**相关论文：** [Multi-Object Tracking in Satellite Videos With Graph-Based Multitask Modeling](https://doi.org/10.1109/TGRS.2022.3152250)

#### MS COCO

**任务方向：** 通用目标检测与分割

大规模通用图像基准，常用于检测、实例分割、关键点和字幕任务。

**关键词：** 通用视觉；检测；分割

**数据与项目入口：** [数据集主页](https://cocodataset.org/)

**补充入口：** [数据下载页](https://cocodataset.org/#download)

**相关论文：** [Microsoft COCO: Common Objects in Context](https://doi.org/10.1007/978-3-319-10602-1_48)

#### UAVDT

**任务方向：** 无人机车辆检测与跟踪

UAVDT（Unmanned Aerial Vehicle Benchmark）面向无人机视角下的交通视频分析，支持车辆检测与跟踪研究。数据涉及拍摄高度、视角、天气、遮挡和目标尺度变化等低空场景因素，可用于检索车辆检测、单目标跟踪和多目标跟踪相关基准资料。

**关键词：** 无人机视频；交通场景；车辆检测；多目标跟踪；尺度变化

**数据与项目入口：** [UAVDT 项目主页](https://sites.google.com/view/grli-uavdt/)

**相关论文：** [The Unmanned Aerial Vehicle Benchmark: Object Detection and Tracking](https://doi.org/10.1007/978-3-030-01249-6_23)

#### DroneVehicle

**任务方向：** RGB—红外车辆检测

DroneVehicle 提供无人机视角的可见光与红外车辆影像，面向跨模态车辆检测研究，可用于查找多光谱信息互补、复杂光照下车辆识别与无人机交通感知相关资料。

**关键词：** 无人机；可见光；红外；跨模态检测；车辆识别

**数据与项目入口：** [项目说明/代码](https://github.com/VisDrone/DroneVehicle)

**相关论文：** [Drone-Based RGB-Infrared Cross-Modality Vehicle Detection via Uncertainty-Aware Learning](https://doi.org/10.1109/TCSVT.2022.3168279)
#### VisDrone

**任务方向：** 无人机视觉综合基准

覆盖检测、跟踪、关键点等任务的无人机视觉数据资源。

**关键词：** 无人机视觉；检测；跟踪

**数据与项目入口：** [项目说明/代码](https://github.com/VisDrone/VisDrone-Dataset)

**补充入口：** [VisDrone 资源主页](https://aiskyeye.com/)

**相关论文：** [VisDrone-DET2021: The Vision Meets Drone Object Detection in Image and Video](https://doi.org/10.1109/ICCVW54120.2021.00319)<br>[VisDrone-MOT2020: The Vision Meets Drone Multiple Object Tracking Challenge Results](https://doi.org/10.1007/978-3-030-66823-5_43)

#### VisDrone-DET

**任务方向：** 航空视频目标检测

无人机视角目标检测基准，包含多类别目标、遮挡与尺度变化。

**关键词：** 目标检测；无人机；航空视频

**数据与项目入口：** [项目说明/代码](https://github.com/VisDrone/VisDrone-Dataset)

**补充入口：** [VisDrone 资源主页](https://aiskyeye.com/)

**相关论文：** [VisDrone-DET2021: The Vision Meets Drone Object Detection in Image and Video](https://doi.org/10.1109/ICCVW54120.2021.00319)

#### VisDrone-MOT

**任务方向：** 航空视频多目标跟踪

与VisDrone系列配套的多目标跟踪数据，提供视频序列和目标轨迹标注。

**关键词：** 多目标跟踪；无人机；视频

**数据与项目入口：** [项目说明/代码](https://github.com/VisDrone/VisDrone-Dataset)

**补充入口：** [VisDrone 资源主页](https://aiskyeye.com/)

**相关论文：** [VisDrone-MOT2020: The Vision Meets Drone Multiple Object Tracking Challenge Results](https://doi.org/10.1007/978-3-030-66823-5_43)

### 语义分割与场景理解

#### SA-1B

**任务方向：** 通用可提示分割数据集

Segment Anything使用的超大规模图像掩模数据资源，适合可提示分割与视觉基础模型研究。

**关键词：** 图像分割；掩模；基础模型

**数据与项目入口：** [SA-1B 数据集主页](https://ai.meta.com/datasets/segment-anything-downloads/)

**补充入口：** [项目说明/代码](https://github.com/facebookresearch/segment-anything)

**相关论文：** [Segment Anything](https://arxiv.org/abs/2304.02643)

#### UAVid

**任务方向：** 航空视频语义分割

高分辨率无人机视频语义分割数据集，强调道路、建筑、车辆等城市场景类别。

**关键词：** 视频分割；无人机；城市

**数据与项目入口：** [UAVid 主页](https://uavid.nl/)

**相关论文：** [UAVid: A Semantic Segmentation Dataset for UAV Imagery](https://doi.org/10.1016/j.isprsjprs.2020.05.009)

#### UDD6

**任务方向：** 无人机道路场景分割

UDD（Urban Drone Dataset）面向无人机城市场景语义分割，发布UDD-3、UDD-5和UDD-6等版本。UDD-6包含立面、道路、植被、车辆、屋顶和其他6类，可用于城市道路场景像素级解析与类别边界识别。项目说明提供Google Drive与百度网盘下载入口；百度网盘提取码为7qua。

**关键词：** 无人机；城市场景；语义分割；立面；道路；植被；车辆；屋顶；其他

**数据与项目入口：** [项目说明/代码](https://github.com/MarcWong/UDD)

**补充入口：** [Google Drive 数据](https://drive.google.com/file/d/1BNL8HNFRiNjSzdcQJo-uXiejZJ6DgunY/view?usp=sharing)<br>[百度网盘数据](https://pan.baidu.com/s/1sQavCwH29PUwTEgF3teMBQ)

**相关论文：** [Large-Scale Structure From Motion With Semantic Constraints of Aerial Images](https://doi.org/10.1007/978-3-030-03398-9_30)

#### FloodNet

**任务方向：** 洪涝灾害场景理解

FloodNet 汇集洪涝灾后无人机航拍影像，支持图像分类、语义分割和视觉问答等场景理解任务，可用于灾害影响判读、受淹区域识别及灾后评估研究。

**关键词：** 洪涝灾害；灾后评估；无人机航拍；语义分割；视觉问答

**数据与项目入口：** [项目说明/代码](https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021)

**相关论文：** [FloodNet: A High Resolution Aerial Imagery Dataset for Post Flood Disaster Assessment](https://doi.org/10.1109/ACCESS.2021.3090981)

### 多模态与遥感数据

#### LuoJiaSET / LuoJia-MVS

**任务方向：** 遥感数据与多视图重建

LuoJiaSET 是武汉大学相关团队发布的遥感数据资源入口，适合查找土地覆盖、变化检测和遥感视觉学习等数据与任务资料；主页同时提供数据说明和相关项目链接。

**关键词：** LuoJiaSET；遥感；土地覆盖；变化检测；视觉学习

**数据与项目入口：** [LuoJiaSET 数据集主页](https://www2.isprs.org/commissions/comm3/wg1/open-resources/luojia-dl-framework/luojiaset/)

**补充入口：** [项目说明/代码](https://github.com/WHULuoJiaTeam/luojiaset)<br>[数据主页](https://gpcv.whu.edu.cn/data/)<br>[数据主页](https://irsip.whu.edu.cn/resources/resources_en_v2.php)

**相关论文：** —

### 三维重建与多视图

#### WHU-MVS / WHU-OMVS

**任务方向：** 多视图立体与三维重建

WHU-OMVS 是面向城市级三维场景重建的斜视航空影像多视图立体数据集，页面提供五相机全向多视影像、深度图和位姿；训练集含27,460张768×384五视角影像，测试集含268张3712×5504真实影像，并提供Ada-MVS实现入口。

**关键词：** WHU-OMVS；多视图立体；斜视航空影像；深度估计；三维重建

**数据与项目入口：** [数据主页](https://gpcv.whu.edu.cn/data/WHU_OMVS_dataset/WHU_dataset.htm)

**补充入口：** [项目说明/代码](https://github.com/gpcv-liujin/Ada-MVS)<br>[数据主页](https://gpcv.whu.edu.cn/data/)

**相关论文：** [Deep learning based multi-view stereo matching and 3D scene reconstruction from oblique aerial images](https://doi.org/10.1016/j.isprsjprs.2023.08.015)

### 无人机导航与具身任务

#### OpenFly / AerialVLN

**任务方向：** 无人机视觉语言导航

OpenFly 是面向空中视觉语言导航的综合平台，项目主页集中展示平台说明、任务设置、数据和实现入口，可用于查找无人机环境观测、语言指令与导航轨迹相关资源。

**关键词：** 视觉语言导航；无人机；具身智能；轨迹

**数据与项目入口：** [项目主页](https://shailab-ipec.github.io/openfly/)

**相关论文：** [Openfly: A comprehensive platform for aerial vision-language navigation](https://arxiv.org/abs/2502.18041)
#### CityNav

**任务方向：** 城市视觉导航

面向真实城市空中导航的大规模数据集，项目页和论文页可用于查找城市航拍观测、导航目标、语言任务与数据发布信息。

**关键词：** CityNav；城市导航；航拍；视觉语言

**数据与项目入口：** [项目主页](https://water-cookie.github.io/city-nav-proj/)

**相关论文：** [CityNav: A Large-Scale Dataset for Real-World Aerial Navigation](https://doi.org/10.1109/ICCV51701.2025.00559)

#### TravelUAV

**任务方向：** 无人机旅行与导航

TRAVEL 是面向真实感无人机视觉语言导航的平台、基准与方法资源；项目页同时提供论文、项目主页、代码、数据集和仿真环境入口，并说明数据准备与模型使用方式。

**关键词：** 无人机；视觉语言导航；仿真平台；TRAVEL；数据集

**数据与项目入口：** [项目说明/代码](https://github.com/buaa-colalab/TravelUAV)

**补充入口：** [OpenUAV 项目主页](https://prince687028.github.io/OpenUAV/)<br>[Hugging Face 数据集](https://huggingface.co/datasets/wangxiangyu0814/TravelUAV)

**相关论文：** [Towards Realistic UAV Vision-Language Navigation: Platform, Benchmark, and Methodology](https://arxiv.org/abs/2410.07087)

## 评价指标与评测代码

本节集中列出综述涉及的评价指标、公开评测项目及本资源包提供的基础代码。每类指标单独列出，便于按任务查找。主页下方提供完整导航，代码示例与运行说明见 [`evaluation/README.md`](evaluation/README.md)。本包的辅助实现用于通用计算示例；目标检测、旋转框/三维检测和挑战赛结果应使用对应数据集或基准的官方评测器。
### 目标检测与精确率/召回率

| 指标 | 说明 | 代码/项目 | 评测协议 | 本包代码 |
| :--- | :--- | :--- | :--- | :--- |
| Precision | 精确率，预测为正的样本中真正例所占比例。 | [代码/项目](https://github.com/scikit-learn/scikit-learn) | [协议/文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| Recall | 召回率，真实正样本中被正确检出的比例。 | [代码/项目](https://github.com/scikit-learn/scikit-learn) | [协议/文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| AP | 平均精度，Precision—Recall曲线下的面积。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| mAP | 各类别AP的平均值。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |
| AP50 | IoU阈值为0.50时的平均精度。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |
| AP75 | IoU阈值为0.75时的平均精度。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |
| APS | 小目标区域上的AP。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |
| APM | 中等目标区域上的AP。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |
| APL | 大目标区域上的AP。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |

### 语义分割与像素分类

| 指标 | 说明 | 代码/项目 | 评测协议 | 本包代码 |
| :--- | :--- | :--- | :--- | :--- |
| IoU | 预测区域或检测框与真值的交集除以并集。 | [代码/项目](https://github.com/Lightning-AI/torchmetrics) | [协议/文档](https://torchmetrics.readthedocs.io/en/stable/classification/jaccard_index.html) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| DSC | Dice相似系数，按两倍交集除以预测区域与真值区域面积之和计算。 | [代码/项目](https://github.com/Lightning-AI/torchmetrics) | [协议/文档](https://lightning.ai/docs/torchmetrics/stable/segmentation/dice.html) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| mIoU | 各类别IoU的平均值。 | [代码/项目](https://github.com/open-mmlab/mmsegmentation) | [协议/文档](https://mmsegmentation.readthedocs.io/en/latest/) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| OA | 整体精度，所有正确分类像素或样本占总数的比例。 | [代码/项目](https://github.com/scikit-learn/scikit-learn) | [协议/文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| Acc | 准确率，按具体任务定义的正确预测比例。 | [代码/项目](https://github.com/scikit-learn/scikit-learn) | [协议/文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| mAcc | 各类别准确率或召回率的平均值，具体沿用基准定义。 | [代码/项目](https://github.com/open-mmlab/mmsegmentation) | [协议/文档](https://mmsegmentation.readthedocs.io/en/latest/) | [`metrics_utils.py`](evaluation/metrics_utils.py) |

### 三维检测、深度与距离

| 指标 | 说明 | 代码/项目 | 评测协议 | 本包代码 |
| :--- | :--- | :--- | :--- | :--- |
| 3D IoU | 三维检测框与三维真值框在空间中的交并比。 | [代码/项目](https://github.com/open-mmlab/mmdetection3d) | [协议/文档](https://mmdetection3d.readthedocs.io/en/latest/advanced_guides/evaluation.html) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| AP3D | 基于三维空间IoU计算的平均精度。 | [代码/项目](https://github.com/open-mmlab/mmdetection3d) | [协议/文档](https://mmdetection3d.readthedocs.io/en/latest/advanced_guides/evaluation.html) | — |
| APBEV | 将三维框投影到鸟瞰图后计算IoU得到的平均精度。 | [代码/项目](https://github.com/open-mmlab/mmdetection3d) | [协议/文档](https://mmdetection3d.readthedocs.io/en/latest/advanced_guides/evaluation.html) | — |
| MAE | 预测值与真值绝对误差的平均值。 | [代码/项目](https://github.com/scikit-learn/scikit-learn) | [协议/文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| <0.6m accuracy | 误差或定位偏差小于0.6 m的样本比例。 | — | — | [`metrics_utils.py`](evaluation/metrics_utils.py) |

### 跟踪与无人机导航

| 指标 | 说明 | 代码/项目 | 评测协议 | 本包代码 |
| :--- | :--- | :--- | :--- | :--- |
| Success | 跟踪结果与真值的重叠度达到不同阈值时形成的成功率曲线或其汇总值。 | [代码/项目](https://github.com/visionml/pytracking) | [协议/文档](https://github.com/visionml/pytracking) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| SR | 导航任务成功率，按目标到达或任务完成条件统计，定义依具体基准。 | [代码/项目](https://github.com/facebookresearch/habitat-lab) | [协议/文档](https://aihabitat.org/challenge/) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| SPL | 路径长度加权成功率，综合任务成功与实际路径效率。 | [代码/项目](https://github.com/facebookresearch/habitat-lab) | [协议/文档](https://aihabitat.org/challenge/) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| MOTA | 综合漏检、误检和身份切换的多目标跟踪准确率。 | [代码/项目](https://github.com/JonathonLuiten/TrackEval) | [协议/文档](https://motchallenge.net/results/MOT17/) | — |
| IDF1 | 身份一致性F1分数，衡量轨迹身份匹配质量。 | [代码/项目](https://github.com/JonathonLuiten/TrackEval) | [协议/文档](https://motchallenge.net/results/MOT17/) | — |

### 模型效率与对比统计

| 指标 | 说明 | 代码/项目 | 评测协议 | 本包代码 |
| :--- | :--- | :--- | :--- | :--- |
| 参数量 | 模型可训练或可推理参数的数量。 | [代码/项目](https://github.com/TylerYep/torchinfo) | [协议/文档](https://github.com/TylerYep/torchinfo) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| FLOPs | 给定输入形状下的浮点运算量估计。 | [代码/项目](https://github.com/facebookresearch/fvcore) | [协议/文档](https://github.com/facebookresearch/fvcore) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| FPS | 单位时间处理的图像或视频帧数。 | — | [协议/文档](https://docs.pytorch.org/docs/stable/benchmark_utils.html) | [`metrics_utils.py`](evaluation/metrics_utils.py) |
| 增益 | 相对于基线或对照模型的指标变化量或相对提升比例。 | — | — | [`metrics_utils.py`](evaluation/metrics_utils.py) |

完整字段、入口和备注见 [`metrics_open_resources.csv`](metrics_open_resources.csv)。

## 论文索引

下表汇总方法/模型与数据集条目中的论文，附研究关键词，便于按模型名、任务或技术主题检索。论文题名链接到论文或出版方页面。

| 名称 | 类型 | 论文题名 | 关键词 |
| :--- | :--- | :--- | :--- |
| Aba-ViTrack | 方法/模型 | [Adaptive and Background-Aware Vision Transformer for Real-Time UAV Tracking](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Adaptive_and_Background-Aware_Vision_Transformer_for_Real-Time_UAV_Tracking_ICCV_2023_paper.pdf) | 视频理解；多目标跟踪；时序建模；运动目标 |
| ALBEF | 方法/模型 | [Align before Fuse: Vision and Language Representation Learning with Momentum Distillation](https://arxiv.org/abs/2107.07651) | 视觉表征；预训练；通用学习；特征提取 |
| ALBERT | 方法/模型 | [ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/abs/1909.11942) | 视觉语言；多模态；图像理解；大模型 |
| ALIGN | 方法/模型 | [Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision](https://arxiv.org/abs/2102.05918) | 视觉语言；多模态；图像理解；大模型 |
| AVTrack | 方法/模型 | [Learning an Adaptive and View-Invariant Vision Transformer for Real-Time UAV Tracking](https://arxiv.org/abs/2412.20002) | 视频理解；多目标跟踪；时序建模；运动目标 |
| Baichuan | 方法/模型 | [Baichuan 2: Open Large-scale Language Models](https://arxiv.org/abs/2309.10305) | 视觉表征；预训练；通用学习；特征提取 |
| BART | 方法/模型 | [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461) | 视觉表征；预训练；通用学习；特征提取 |
| BDTrack | 方法/模型 | [Learning Motion Blur Robust Vision Transformers for Real-Time UAV Tracking](https://arxiv.org/abs/2407.05383) | 视频理解；多目标跟踪；时序建模；运动目标 |
| BEiT | 方法/模型 | [BEiT: BERT Pre-Training of Image Transformers](https://arxiv.org/abs/2106.08254) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| BERT | 方法/模型 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | 视觉语言；多模态；图像理解；大模型 |
| BLIP | 方法/模型 | [BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](https://arxiv.org/abs/2201.12086) | 视觉语言；多模态；图像理解；大模型 |
| BLIP-2 | 方法/模型 | [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597) | 视觉语言；多模态；图像理解；大模型 |
| BYOL | 方法/模型 | [Bootstrap your own latent: A new approach to self-supervised Learning](https://arxiv.org/abs/2006.07733) | 视觉表征；预训练；通用学习；特征提取 |
| ByteTrack | 方法/模型 | [ByteTrack: Multi-Object Tracking by Associating Every Detection Box](https://arxiv.org/abs/2110.06864) | 视频理解；多目标跟踪；时序建模；运动目标 |
| CenterTrack | 方法/模型 | [CenterTrack: Tracking Objects as Points](https://arxiv.org/abs/2004.01177) | 视频理解；多目标跟踪；时序建模；运动目标 |
| Chameleon | 方法/模型 | [Chameleon: Mixed-Modal Early-Fusion Foundation Models](https://arxiv.org/abs/2405.09818) | 视觉表征；预训练；通用学习；特征提取 |
| Change-Agent | 方法/模型 | [Change-Agent: Towards Interactive Comprehensive Remote Sensing Change Interpretation and Analysis](https://arxiv.org/abs/2403.19646) | 无人机；视觉语言导航；具身智能；路径规划 |
| CityNavAgent | 方法/模型 | [CityNavAgent: Aerial Vision-and-Language Navigation With Hierarchical Semantic Planning and Global Memory](https://doi.org/10.18653/v1/2025.acl-long.1511) | 无人机；视觉语言导航；具身智能；路径规划 |
| CLIP | 方法/模型 | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | 视觉语言；多模态；图像理解；大模型 |
| CoCa | 方法/模型 | [CoCa: Contrastive Captioners are Image-Text Foundation Models](https://arxiv.org/abs/2205.01917) | 视觉表征；预训练；通用学习；特征提取 |
| CogVLM | 方法/模型 | [CogVLM: Visual Expert for Pretrained Language Models](https://arxiv.org/abs/2311.03079) | 视觉语言；多模态；图像理解；大模型 |
| ConSERT | 方法/模型 | [ConSERT: A Contrastive Framework for Self-Supervised Sentence Representation Transfer](https://arxiv.org/abs/2105.11741) | 视觉表征；预训练；通用学习；特征提取 |
| CSP | 方法/模型 | [CSP: Self-Supervised Contrastive Spatial Pre-Training for Geospatial-Visual Representations](https://arxiv.org/abs/2305.01118) | 视觉表征；预训练；通用学习；特征提取 |
| DDQ-DETR | 方法/模型 | [Dense Distinct Query for End-to-End Object Detection](https://arxiv.org/abs/2303.12776) | 目标检测；开放词汇；视觉定位；小目标 |
| DeBERTa | 方法/模型 | [DeBERTa: Decoding-enhanced BERT with Disentangled Attention](https://arxiv.org/abs/2006.03654) | 视觉语言；多模态；图像理解；大模型 |
| DeepLabV3+ | 方法/模型 | [Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1802.02611) | 语义分割；实例分割；像素级理解；边界恢复 |
| DeepSeek | 方法/模型 | [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) | 视觉表征；预训练；通用学习；特征提取 |
| DeepSeek-VL | 方法/模型 | [DeepSeek-VL: Towards Real-World Vision-Language Understanding](https://arxiv.org/abs/2403.05525) | 视觉语言；多模态；图像理解；大模型 |
| Detic | 方法/模型 | [Detecting Twenty-thousand Classes using Image-level Supervision](https://arxiv.org/abs/2201.02605) | 目标检测；开放词汇；视觉定位；小目标 |
| DETR | 方法/模型 | [End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872) | 目标检测；开放词汇；视觉定位；小目标 |
| DGTRS-CLIP | 方法/模型 | [DGTRSD & DGTRS-CLIP: A Dual-Granularity Remote Sensing Image-Text Dataset and Vision Language Foundation Model for Alignment](https://arxiv.org/abs/2503.19311) | 视觉语言；多模态；图像理解；大模型 |
| DiffCSE | 方法/模型 | [DiffCSE: Difference-based Contrastive Learning for Sentence Embeddings](https://arxiv.org/abs/2204.10298) | 视觉表征；预训练；通用学习；特征提取 |
| DINO | 方法/模型 | [DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection](https://arxiv.org/abs/2203.03605) | 目标检测；开放词汇；视觉定位；小目标 |
| DINOv2 | 方法/模型 | [DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193) | 视觉表征；预训练；通用学习；特征提取 |
| DOFA-CLIP | 方法/模型 | [DOFA-CLIP: Multimodal Vision-Language Foundation Models for Earth Observation](https://arxiv.org/abs/2503.06312) | 视觉语言；多模态；图像理解；大模型 |
| DRCI | 方法/模型 | [Towards Discriminative Representations with Contrastive Instances for Real-Time UAV Tracking](https://arxiv.org/abs/2308.11450) | 视觉表征；预训练；通用学习；特征提取 |
| DualToken | 方法/模型 | [DualToken: Towards Unifying Visual Understanding and Generation with Dual Visual Vocabularies](https://arxiv.org/abs/2503.14324) | 视觉表征；预训练；通用学习；特征提取 |
| EarthGPT | 方法/模型 | [EarthGPT: A Universal Multimodal Large Language Model for Multisensor Image Comprehension in Remote Sensing Domain](https://doi.org/10.1109/TGRS.2024.3409624) | 多传感器；视觉语言；遥感问答；多模态大模型 |
| EarthGPT-X | 方法/模型 | [EarthGPT-X: A Spatial MLLM for Multilevel Multisource Remote Sensing Imagery Understanding With Visual Prompting](https://doi.org/10.1109/TGRS.2025.3626941) | 多源遥感；空间理解；视觉提示；多模态大模型 |
| ELECTRA | 方法/模型 | [ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators](https://arxiv.org/abs/2003.10555) | 视觉表征；预训练；通用学习；特征提取 |
| Falcon | 方法/模型 | [Falcon: A Remote Sensing Vision-Language Foundation Model (Technical Report)](https://arxiv.org/abs/2503.11070) | 视觉表征；预训练；通用学习；特征提取 |
| FBRT-YOLO | 方法/模型 | [FBRT-YOLO: Faster and Better for Real-Time Aerial Image Detection](https://doi.org/10.1609/aaai.v39i8.32937) | 实时检测；航空影像；YOLO；轻量化 |
| FILIP | 方法/模型 | [FILIP: Fine-grained Interactive Language-Image Pre-Training](https://arxiv.org/abs/2111.07783) | 视觉表征；预训练；通用学习；特征提取 |
| FLAVA | 方法/模型 | [FLAVA: A Foundational Language And Vision Alignment Model](https://arxiv.org/abs/2112.04482) | 视觉语言；多模态；图像理解；大模型 |
| FlightGPT | 方法/模型 | [FlightGPT: Towards Generalizable and Interpretable UAV Vision-and-Language Navigation With Vision-Language Models](https://doi.org/10.18653/v1/2025.emnlp-main.338) | 无人机；视觉语言导航；具身智能；路径规划 |
| FLIP | 方法/模型 | [Scaling Language-Image Pre-training via Masking](https://arxiv.org/abs/2212.00794) | 视觉表征；预训练；通用学习；特征提取 |
| GeoChat | 方法/模型 | [GeoChat: Grounded Large Vision-Language Model for Remote Sensing](https://arxiv.org/abs/2311.15826) | 视觉语言；多模态；图像理解；大模型 |
| GeoCLIP | 方法/模型 | [GeoCLIP: Clip-Inspired Alignment between Locations and Images for Effective Worldwide Geo-localization](https://arxiv.org/abs/2309.16020v2) | 视觉语言；多模态；图像理解；大模型 |
| GeoPixel | 方法/模型 | [GeoPixel: Pixel Grounding Large Multimodal Model in Remote Sensing](https://arxiv.org/abs/2501.13925) | 视觉表征；预训练；通用学习；特征提取 |
| GLIP | 方法/模型 | [Grounded Language-Image Pre-training](https://arxiv.org/abs/2112.03857) | 视觉表征；预训练；通用学习；特征提取 |
| GLM | 方法/模型 | [GLM-130B: An Open Bilingual Pre-trained Model](https://arxiv.org/abs/2210.02414) | 视觉语言；多模态；图像理解；大模型 |
| GPT | 方法/模型 | [Improving Language Understanding by Generative Pre-Training](https://www.mikecaptain.com/resources/pdf/GPT-1.pdf) | 视觉语言；多模态；图像理解；大模型 |
| Grounding DINO | 方法/模型 | [Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection](https://arxiv.org/abs/2303.05499) | 目标检测；开放词汇；视觉定位；小目标 |
| HRNet | 方法/模型 | [Deep High-Resolution Representation Learning for Visual Recognition](https://arxiv.org/abs/1908.07919) | 语义分割；实例分割；像素级理解；边界恢复 |
| HYDRA | 方法/模型 | [HYDRA: A Hyper Agent for Dynamic Compositional Visual Reasoning](https://link.springer.com/chapter/10.1007/978-3-031-72661-3_8) | 视觉表征；预训练；通用学习；特征提取 |
| HyperSIGMA | 方法/模型 | [HyperSIGMA: Hyperspectral Intelligence Comprehension Foundation Model](https://arxiv.org/abs/2406.11519) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| iGPT | 方法/模型 | [Generative Pretraining from Pixels](https://cdn.openai.com/papers/Generative_Pretraining_from_Pixels_V2.pdf) | 视觉语言；多模态；图像理解；大模型 |
| ImageBind | 方法/模型 | [ImageBind: One Embedding Space To Bind Them All](https://arxiv.org/abs/2305.05665) | 视觉语言；多模态；图像理解；大模型 |
| InternLM | 方法/模型 | [InternLM2 Technical Report](https://arxiv.org/abs/2403.17297) | 大语言模型；开源模型；长上下文；预训练 |
| InternVL | 方法/模型 | [InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks](https://arxiv.org/abs/2312.14238) | 视觉语言；多模态；图像理解；大模型 |
| K-Lite | 方法/模型 | [K-LITE: Learning Transferable Visual Models with External Knowledge](https://arxiv.org/abs/2204.09222) | 视觉表征；预训练；通用学习；特征提取 |
| LaCLIP | 方法/模型 | [Improving CLIP Training with Language Rewrites](https://arxiv.org/abs/2305.20088) | 视觉语言；多模态；图像理解；大模型 |
| LeMeViT | 方法/模型 | [LeMeViT: Efficient Vision Transformer with Learnable Meta Tokens for Remote Sensing Image Interpretation](https://arxiv.org/abs/2405.09789) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| LiT | 方法/模型 | [LiT: Zero-Shot Transfer with Locked-image text Tuning](https://arxiv.org/abs/2111.07991) | 视觉表征；预训练；通用学习；特征提取 |
| LLaMA | 方法/模型 | [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) | 视觉表征；预训练；通用学习；特征提取 |
| LLaMA-VID | 方法/模型 | [LLaMA-VID: An Image is Worth 2 Tokens in Large Language Models](https://arxiv.org/abs/2311.17043) | 视觉语言；多模态；图像理解；大模型 |
| LLaVA | 方法/模型 | [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485) | 视觉语言；多模态；图像理解；大模型 |
| LLaVA-1.5 | 方法/模型 | [Improved Baselines with Visual Instruction Tuning](https://arxiv.org/abs/2310.03744) | 视觉语言；多模态；图像理解；大模型 |
| LLaVA-CoT | 方法/模型 | [LLaVA-CoT: Let Vision Language Models Reason Step-by-Step](https://arxiv.org/abs/2411.10440) | 视觉语言；多模态；图像理解；大模型 |
| LongFly | 方法/模型 | [LongFly: Long-Horizon UAV Vision-and-Language Navigation with Spatiotemporal Context Integration](https://arxiv.org/abs/2512.22010) | 无人机；视觉语言导航；具身智能；路径规划 |
| LXMERT | 方法/模型 | [LXMERT: Learning Cross-Modality Encoder Representations from Transformers](https://arxiv.org/abs/1908.07490) | 视觉表征；预训练；通用学习；特征提取 |
| MA3E | 方法/模型 | [Masked Angle-Aware Autoencoder for Remote Sensing Images](https://arxiv.org/abs/2408.01946) | 视觉表征；预训练；通用学习；特征提取 |
| MAE | 方法/模型 | [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| MAGE | 方法/模型 | [MAGE: Masked Generative Encoder to Unify Representation Learning and Image Synthesis](https://ieeexplore.ieee.org/document/10203945/) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| MaskFeat | 方法/模型 | [Masked Feature Prediction for Self-Supervised Visual Pre-Training](https://arxiv.org/abs/2112.09133) | 语义分割；实例分割；像素级理解；边界恢复 |
| MaskGIT | 方法/模型 | [MaskGIT: Masked Generative Image Transformer](https://arxiv.org/abs/2202.04200) | 语义分割；实例分割；像素级理解；边界恢复 |
| MASS | 方法/模型 | [MASS: Masked Sequence to Sequence Pre-training for Language Generation](https://arxiv.org/abs/1905.02450) | 视觉表征；预训练；通用学习；特征提取 |
| Megatron-LM | 方法/模型 | [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053) | 视觉表征；预训练；通用学习；特征提取 |
| MetaMorph | 方法/模型 | [MetaMorph: Multimodal Understanding and Generation via Instruction Tuning](https://arxiv.org/abs/2412.14164) | 视频理解；时序表征；掩码建模；视频预训练 |
| Mini-Gemini | 方法/模型 | [Mini-Gemini: Mining the Potential of Multi-modality Vision Language Models](https://arxiv.org/abs/2403.18814) | 视觉表征；预训练；通用学习；特征提取 |
| MM-Interleaved | 方法/模型 | [MM-Interleaved: Interleaved Image-Text Generative Modeling via Multi-modal Feature Synchronizer](https://arxiv.org/abs/2401.10208) | 视觉表征；预训练；通用学习；特征提取 |
| MoCo | 方法/模型 | [Momentum Contrast for Unsupervised Visual Representation Learning](https://arxiv.org/abs/1911.05722) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| MoE-LLaVA | 方法/模型 | [MoE-LLaVA: Mixture of Experts for Large Vision-Language Models](https://arxiv.org/abs/2401.15947) | 视觉语言；多模态；图像理解；大模型 |
| MSN | 方法/模型 | [Masked Siamese Networks for Label-Efficient Learning](https://arxiv.org/abs/2204.07141) | 视觉表征；预训练；通用学习；特征提取 |
| mT5 | 方法/模型 | [mT5: A massively multilingual pre-trained text-to-text transformer](https://arxiv.org/abs/2010.11934) | 视觉语言；多模态；图像理解；大模型 |
| NavAgent | 方法/模型 | [NavAgent: Multi-scale Urban Street View Fusion For UAV Embodied Vision-and-Language Navigation](https://arxiv.org/abs/2411.08579) | 无人机；视觉语言导航；具身智能；路径规划 |
| OGMN | 方法/模型 | [OGMN: Occlusion-guided Multi-task Network for Object Detection in UAV Images](https://arxiv.org/abs/2304.11805) | 目标检测；开放词汇；视觉定位；小目标 |
| OpenFly-Agent | 方法/模型 | [Openfly: A comprehensive platform for aerial vision-language navigation](https://arxiv.org/abs/2502.18041) | 无人机视觉语言导航；环境模拟；轨迹；具身智能 |
| ORTrack | 方法/模型 | [Learning Occlusion-Robust Vision Transformers for Real-Time UAV Tracking](https://arxiv.org/abs/2504.09228) | 视频理解；多目标跟踪；时序建模；运动目标 |
| OSCAR | 方法/模型 | [Oscar: Object-Semantics Aligned Pre-training for Vision-Language Tasks](https://arxiv.org/abs/2004.06165) | 视觉表征；预训练；通用学习；特征提取 |
| OWL-ViT | 方法/模型 | [Simple Open-Vocabulary Object Detection with Vision Transformers](https://arxiv.org/abs/2205.06230) | 目标检测；开放词汇；视觉定位；小目标 |
| OWLv2 | 方法/模型 | [Scaling Open-Vocabulary Object Detection](https://arxiv.org/abs/2306.09683) | 目标检测；开放词汇；视觉定位；小目标 |
| Pixel-BERT | 方法/模型 | [Pixel-BERT: Aligning Image Pixels with Text by Deep Multi-Modal Transformers](https://arxiv.org/abs/2004.00849) | 视觉语言；多模态；图像理解；大模型 |
| PromptBERT | 方法/模型 | [PromptBERT: Improving BERT Sentence Embeddings with Prompts](https://arxiv.org/abs/2201.04337) | 视觉语言；多模态；图像理解；大模型 |
| PVT | 方法/模型 | [Pyramid Vision Transformer: A Versatile Backbone for Dense Prediction without Convolutions](https://arxiv.org/abs/2102.12122) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| Qwen | 方法/模型 | [Qwen Technical Report](https://arxiv.org/abs/2309.16609) | 视觉语言；多模态；图像理解；大模型 |
| Qwen-VL | 方法/模型 | [Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond](https://arxiv.org/abs/2308.12966) | 视觉语言；多模态；图像理解；大模型 |
| RACF | 方法/模型 | [Learning residue-aware correlation filters and refining scale for real-time UAV tracking](https://doi.org/10.1016/j.patcog.2022.108614) | 视觉表征；预训练；通用学习；特征提取 |
| RegionCLIP | 方法/模型 | [RegionCLIP: Region-based Language-Image Pretraining](https://arxiv.org/abs/2112.09106) | 视觉语言；多模态；图像理解；大模型 |
| Remote Sense ChatGPT | 方法/模型 | [Remote Sensing ChatGPT: Solving Remote Sensing Tasks With ChatGPT and Visual Models](https://doi.org/10.1109/IGARSS53475.2024.10640736) | 遥感视觉问答；视觉语言；多模态；任务泛化 |
| RemoteCLIP | 方法/模型 | [RemoteCLIP: A Vision Language Foundation Model for Remote Sensing](https://arxiv.org/abs/2306.11029) | 视觉语言；多模态；图像理解；大模型 |
| RetinaNet | 方法/模型 | [Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002) | 目标检测；开放词汇；视觉定位；小目标 |
| RingMo-Aerial | 方法/模型 | [RingMo-Aerial: An Aerial Remote Sensing Foundation Model With Affine Transformation Contrastive Learning](https://doi.org/10.1109/TPAMI.2025.3602237) | 航空遥感；视觉基础模型；仿射变换；对比学习 |
| RoBERTa | 方法/模型 | [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692) | 视觉语言；多模态；图像理解；大模型 |
| RS-Agent | 方法/模型 | [RS-Agent: Automating Remote Sensing Tasks through Intelligent Agent](https://arxiv.org/abs/2406.07089) | 无人机；视觉语言导航；具身智能；路径规划 |
| RSPrompter | 方法/模型 | [RSPrompter: Learning to Prompt for Remote Sensing Instance Segmentation based on Visual Foundation Model](https://arxiv.org/abs/2306.16269) | 语义分割；实例分割；像素级理解；边界恢复 |
| RVSA | 方法/模型 | [Advancing Plain Vision Transformer Towards Remote Sensing Foundation Model](https://arxiv.org/abs/2208.03987) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| SAM | 方法/模型 | [Segment Anything](https://arxiv.org/abs/2304.02643) | 语义分割；实例分割；像素级理解；边界恢复 |
| SAM-Track | 方法/模型 | [Segment and Track Anything](https://arxiv.org/abs/2305.06558) | 视频理解；多目标跟踪；时序建模；运动目标 |
| SARATR-X | 方法/模型 | [SARATR-X: Toward Building A Foundation Model for SAR Target Recognition](https://arxiv.org/abs/2405.09365) | 视觉表征；预训练；通用学习；特征提取 |
| SatCLIP | 方法/模型 | [SatCLIP: Global, General-Purpose Location Embeddings with Satellite Imagery](https://arxiv.org/abs/2311.17179) | 视觉语言；多模态；图像理解；大模型 |
| SatMAE | 方法/模型 | [SatMAE: Pre-training Transformers for Temporal and Multi-Spectral Satellite Imagery](https://arxiv.org/abs/2207.08051) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| Scale-MAE | 方法/模型 | [Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning](https://arxiv.org/abs/2212.14532) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| SDST | 方法/模型 | [SDST: Self-Supervised Double-Structure Transformer for Hyperspectral Images Clustering](https://ieeexplore.ieee.org/document/10462168) | 视觉表征；预训练；通用学习；特征提取 |
| SimCLR | 方法/模型 | [A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2002.05709) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| SimCSE | 方法/模型 | [SimCSE: Simple Contrastive Learning of Sentence Embeddings](https://doi.org/10.18653/v1/2021.emnlp-main.552) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| SimMIM | 方法/模型 | [SimMIM: A Simple Framework for Masked Image Modeling](https://arxiv.org/abs/2111.09886) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| SPAR | 方法/模型 | [Self-Prompting Analogical Reasoning for UAV Object Detection](https://doi.org/10.1609/aaai.v39i17.34026) | 无人机检测；自提示；类比推理；小目标 |
| SwAV | 方法/模型 | [Unsupervised Learning of Visual Features by Contrasting Cluster Assignments](https://arxiv.org/abs/2006.09882) | 视觉表征；预训练；通用学习；特征提取 |
| T5 | 方法/模型 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683) | 视觉语言；多模态；图像理解；大模型 |
| Text2Earth | 方法/模型 | [Text2Earth: Unlocking Text-driven Remote Sensing Image Generation with a Global-Scale Dataset and a Foundation Model](https://doi.org/10.1109/MGRS.2025.3560455) | 文本到图像生成；遥感基础模型；全球尺度数据集 |
| Tree-GPT | 方法/模型 | [TREE-GPT: Modular Large Language Model Expert System for Forest Remote Sensing Image Understanding and Interactive Analysis](https://doi.org/10.5194/isprs-archives-XLVIII-1-W2-2023-1729-2023) | 视觉语言；多模态；图像理解；大模型 |
| UAV-DETR | 方法/模型 | [UAV-DETR: Efficient End-to-End Object Detection for Unmanned Aerial Vehicle Imagery](https://doi.org/10.1109/IROS60139.2025.11246176) | 无人机检测；端到端检测；Transformer；小目标 |
| UAV-VLN | 方法/模型 | [UAV-VLN: End-to-End Vision Language Guided Navigation for UAVs](https://doi.org/10.1109/ECMR65884.2025.11163198) | 无人机导航；视觉语言；路径规划；具身智能 |
| UAVFormer | 方法/模型 | [UAVformer: A Composite Transformer Network for Urban Scene Segmentation of UAV Images](https://doi.org/10.1016/j.patcog.2022.109019) | 无人机语义分割；Transformer；城市场景；像素级理解 |
| UniLM | 方法/模型 | [Unified Language Model Pre-training for Natural Language Understanding and Generation](https://arxiv.org/abs/1905.03197) | 视觉表征；预训练；通用学习；特征提取 |
| UNIMO | 方法/模型 | [UNIMO: Towards Unified-Modal Understanding and Generation via Cross-Modal Contrastive Learning](https://arxiv.org/abs/2012.15409) | 视觉表征；预训练；通用学习；特征提取 |
| UNIT | 方法/模型 | [UNIT: Unifying Image and Text Recognition in One Vision Encoder](https://arxiv.org/abs/2409.04095) | 视觉表征；预训练；通用学习；特征提取 |
| UNITER | 方法/模型 | [UNITER: UNiversal Image-TExt Representation Learning](https://arxiv.org/abs/1909.11740) | 视觉表征；预训练；通用学习；特征提取 |
| USat | 方法/模型 | [USat: A Unified Self-Supervised Encoder for Multi-Sensor Satellite Imagery](https://arxiv.org/abs/2312.02199) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| Video-ChatGPT | 方法/模型 | [Video-ChatGPT: Towards Detailed Video Understanding via Large Vision and Language Models](https://arxiv.org/abs/2306.05424) | 视觉语言；多模态；图像理解；大模型 |
| VideoMAE | 方法/模型 | [VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training](https://arxiv.org/abs/2203.12602) | 视频理解；时序表征；掩码建模；视频预训练 |
| VideoMAEv2 | 方法/模型 | [VideoMAE V2: Scaling Video Masked Autoencoders with Dual Masking](https://arxiv.org/abs/2303.16727) | 视频理解；时序表征；掩码建模；视频预训练 |
| VideoTree | 方法/模型 | [VideoTree: Adaptive Tree-based Video Representation for LLM Reasoning on Long Videos](https://arxiv.org/abs/2405.19209) | 视频理解；时序表征；掩码建模；视频预训练 |
| VinVL | 方法/模型 | [VinVL: Revisiting Visual Representations in Vision-Language Models](https://arxiv.org/abs/2101.00529) | 视觉语言；多模态；图像理解；大模型 |
| VISPROG | 方法/模型 | [Visual Programming: Compositional visual reasoning without training](https://arxiv.org/abs/2211.11559) | 视觉语言；多模态；图像理解；大模型 |
| ViT | 方法/模型 | [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) | 遥感预训练；视觉表征；自监督学习；跨模态 |
| VLMo | 方法/模型 | [VLMo: Unified Vision-Language Pre-Training With Mixture-of-Modality-Experts](https://arxiv.org/abs/2111.02358) | 视觉语言；多模态；图像理解；大模型 |
| VQGAN | 方法/模型 | [Taming Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2012.09841) | 视觉表征；预训练；通用学习；特征提取 |
| X-VLM | 方法/模型 | [Multi-Grained Vision Language Pre-Training: Aligning Texts with Visual Concepts](https://arxiv.org/abs/2111.08276) | 视觉语言；多模态；图像理解；大模型 |
| XLM | 方法/模型 | [Cross-lingual Language Model Pretraining](https://arxiv.org/abs/1901.07291) | 视觉表征；预训练；通用学习；特征提取 |
| XLNet | 方法/模型 | [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237) | 视觉表征；预训练；通用学习；特征提取 |
| AerialSARData | 数据集/基准 | [RingMo-Aerial: An Aerial Remote Sensing Foundation Model With Affine Transformation Contrastive Learning](https://doi.org/10.1109/TPAMI.2025.3602237) | SAR；航空遥感；车辆检测；无人机；RingMo-Aerial |
| AI-TOD | 数据集/基准 | [A Normalized Gaussian Wasserstein Distance for Tiny Object Detection](https://arxiv.org/abs/2110.13389) | AI-TOD；小目标；航空影像；检测；密集目标 |
| AIR-MOT | 数据集/基准 | [Multi-Object Tracking in Satellite Videos With Graph-Based Multitask Modeling](https://doi.org/10.1109/TGRS.2022.3152250) | 多目标跟踪；卫星视频；AIR-MOT；图结构 |
| CityNav | 数据集/基准 | [CityNav: A Large-Scale Dataset for Real-World Aerial Navigation](https://doi.org/10.1109/ICCV51701.2025.00559) | CityNav；城市导航；航拍；视觉语言 |
| DroneVehicle | 数据集/基准 | [Drone-Based RGB-Infrared Cross-Modality Vehicle Detection via Uncertainty-Aware Learning](https://doi.org/10.1109/TCSVT.2022.3168279) | 可见光；红外；车辆检测 |
| FloodNet | 数据集/基准 | [FloodNet: A High Resolution Aerial Imagery Dataset for Post Flood Disaster Assessment](https://doi.org/10.1109/ACCESS.2021.3090981) | 洪涝；灾害评估；分割 |
| MS COCO | 数据集/基准 | [Microsoft COCO: Common Objects in Context](https://doi.org/10.1007/978-3-319-10602-1_48) | 通用视觉；检测；分割 |
| OpenFly / AerialVLN | 数据集/基准 | [Openfly: A comprehensive platform for aerial vision-language navigation](https://arxiv.org/abs/2502.18041) | 视觉语言导航；无人机；具身智能；轨迹 |
| SA-1B | 数据集/基准 | [Segment Anything](https://arxiv.org/abs/2304.02643) | 图像分割；掩模；基础模型 |
| TravelUAV | 数据集/基准 | [Towards Realistic UAV Vision-Language Navigation: Platform, Benchmark, and Methodology](https://arxiv.org/abs/2410.07087) | 无人机；视觉语言导航；仿真平台；TRAVEL；数据集 |
| UAVDT | 数据集/基准 | [The Unmanned Aerial Vehicle Benchmark: Object Detection and Tracking](https://doi.org/10.1007/978-3-030-01249-6_23) | 车辆；检测；跟踪；无人机 |
| UAVid | 数据集/基准 | [UAVid: A Semantic Segmentation Dataset for UAV Imagery](https://doi.org/10.1016/j.isprsjprs.2020.05.009) | 视频分割；无人机；城市 |
| UDD6 | 数据集/基准 | [Large-Scale Structure From Motion With Semantic Constraints of Aerial Images](https://doi.org/10.1007/978-3-030-03398-9_30) | 道路；语义分割；无人机；UDD-5；UDD-6 |
| VisDrone | 数据集/基准 | [VisDrone-DET2021: The Vision Meets Drone Object Detection in Image and Video](https://doi.org/10.1109/ICCVW54120.2021.00319) | 无人机视觉；检测；跟踪 |
| VisDrone-DET | 数据集/基准 | [VisDrone-DET2021: The Vision Meets Drone Object Detection in Image and Video](https://doi.org/10.1109/ICCVW54120.2021.00319) | 目标检测；无人机；航空视频 |
| VisDrone-MOT | 数据集/基准 | [VisDrone-MOT2020: The Vision Meets Drone Multiple Object Tracking Challenge Results](https://doi.org/10.1007/978-3-030-66823-5_43) | 多目标跟踪；无人机；视频 |
| WHU-MVS / WHU-OMVS | 数据集/基准 | [Deep learning based multi-view stereo matching and 3D scene reconstruction from oblique aerial images](https://doi.org/10.1016/j.isprsjprs.2023.08.015) | WHU-OMVS；多视图立体；斜视航空影像；深度估计；三维重建 |

## 引用与使用说明

1. 使用某项方法、模型或数据集时，请优先引用对应论文，并遵循作者、项目团队或数据发布方页面中的引用要求。
2. 本主页提供论文、代码、项目和数据入口，不在压缩包中再分发第三方数据、图像、标注、模型权重、论文全文或代码。
3. 数据、模型和代码的具体版本、访问方式及使用条件以链接指向的发布页面为准。


## 文件说明

| 文件 | 内容 |
| :--- | :--- |
| README.md | 展示完整的方法、数据集与论文索引 |
| methods_open_resources.csv | 方法/模型、研究方向、关键词及论文和项目入口 |
| datasets_open_resources.csv | 数据集简介、多个入口和相关论文 |
| papers_index.csv | 论文题名、关键词和论文入口索引 |
| evaluation/README.md | 评价指标分类、代码入口、运行方式与使用边界 |
| evaluation/metrics_utils.py | 通用指标与效率统计基础代码 |
| evaluation/test_metrics_utils.py | 8项自动化回归测试 |
| metrics_open_resources.csv | 29项评价指标、代码入口和评测协议入口 |
| manifest.json | 资源包名称、版本和条目数量 |
| checksums_sha256.csv | 包内文件SHA-256校验值 |






