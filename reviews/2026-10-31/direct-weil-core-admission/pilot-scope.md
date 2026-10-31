# 原448阶实际Llow中心谱：一次数值实验，sign未决

2026-10-31；`/root/whole_weil_matrix_input` 的新followup任务。先前`matrix-input-audit.md`保持6803 bytes、SHA256 `6b94561b7502c3327434c2339247a9c732b017431e019bb767a0e7281e5ac3a7`不改；它记录的是当时未获不同可判门的输入审计。随后parent明确授权一个不同counterfactual：**新实际Llow负方向**若获严格证书，可否定whole Llow；positive head则不能证明whole Q。故本次只运行原冻结N448、两个224-sector的一次中心谱pilot，不扫描小head或其它参数。

## 实际对象与原norm

原L9/8、Omega256、N448及既有source不变，令C为Llow=M+Kcompact+U在原Legendre空间的du正交规范压缩。不是P₀、Kcert、旧trial或旧witness。

直接读取旧source矩阵的A/J0及尾列，使用旧physical-gate的实际serialized约定：

    C=Γdu^(-1/2)[(Aint+J0int)/2^257
           +36 Σcol tint_col tint_col*/2^1282]Γdu^(-1/2),
    Γdu,jj=9/[4(2j+1)], tint=midTwice=lo+hi.

不能将serialized尾列再乘81/27；这些归一因子已由其raw列定义和系数36处理。Γdu不是Dlog Gram。源是原physical r=e^(u/2)bare，finite Legendre零延拓在Dlog域；新脚本不读旧v/P₀/trial、未调用旧calculate。原pp2/3/4/5/7/8/9、compact Γ/contact及双pole在既定source中；Llow仅保rank-two U，不包含完整未用Fourier tail。

## 唯一执行与观测

使用bundled Python、NumPy2.3.5，float64装配中心矩阵，分别一次`numpy.linalg.eigh`完成两个完整224块。脚本内计时0.249秒、进程exit0；没有live session/handle。SciPy未安装，未安装或下载任何依赖。旧输入在运行前后均重核SHA，原6803byte审计未变。

| sector | 最小中心eigenvalue | 最小pair的L2 residual | matrix infinity norm |
|---|---:|---:|---:|
| even | -8.625085858788997e-16 | 4.526628301065081e-15 | 18.00287958138488 |
| odd | -2.5645172493272076e-16 | 3.735755676875819e-15 | 17.882118359759815 |

各块均有2个负float值、6个值落在脚本的描述性screen约1.8e-9内，没有值低于负screen。该screen是预设数值筛查量，**不是rigorous误差界**；residual同样是float计算，不能据此证明真实C的sign。JSON保存最低16个中心值、norm/residual、native/同方向raw源float系数及全部输入hash。

旧all-source source费用为epsilon_low=2^-204+2·2^-220+9·2^-512，但这不支付本次float转换、矩阵装配及eigensolver的误差。观察到的极小负值处于本次计算的roundoff/residual尺度；本稿不把它升级为interval负方向，也不称positive head通过，更不称whole Llow/Q正或负。

## 停止与交付

本次结论是**EXPERIMENT／sign未决**：新实际C的center谱已观测，但没有带严格负余量的新输入。一次pilot预算已用完；不自动提高精度、另取方向、构造exact证书、改rank/配置或续旧inverse/Gram链。即使head日后严格为正，原whole coupling仍须另付。

新产物：`actual-lowlow-spectrum-pilot.py`（9439 bytes，SHA256 `fb305e77bb3a348d108dab7fa605d94c58abf0ea3fbf1cbc843e8c234e330f45`）及JSON（33938 bytes，SHA256 `fe78847d24b8be5cb9696d68e51c8b2f4bec90d3d3b622bfc59f9e753e23ac6d`）。未重建source、调用compiler、重放595v、改旧文件、STATE、cadence、库、Goal或Git。本实验不自行授C067/604，不计数学轮，不改变原长期完成门。
