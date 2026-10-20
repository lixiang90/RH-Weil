# 实际变分来源门：fresh 数学与前件终审

2026-10-20。独立终审，只写本文件；不改公共 STATE、cadence、Goal 或 Git，不另计数学轮。
恢复 README/STATE、check/show、同 G20261014／0c4f≤538、C035、D20261020P、宏观前沿和新路线图§4。
现场三原稿及主报告已落盘，本审检查其真实证明，不把原件出稿或 hash 当作 root 消费。

**结论：PASS，可按主报告的固定安全高频范围消费。无阻塞修订。**
原域、signed interval 的全部尾、clipping、两个完整平方和系数方向、真实 cross-tail、
actual 密度及原 du 高频误差运输均闭合；这是一项旧资产的明确直接合成。
不能消费为572所有 θ>2e 的运输、全源小费、危险核心、独立容量或新的 whole 结果。
按用户停止规则，本门保存本范围即停止；不建 C036，不改原 cadence，不续阈值参数。

## 1. 核读范围与独立组织

本审重新核读当前主报告及三份原稿全文，并实际核读以下必要原件：

- 532 §§2–3：完整 Γ 的 Fourier 相位证明、ALL 有限区间且常数独立位置／长度的 clipping、裸求值 k_R。
- 560 全文，及 `joint-sonin-cross/full-inverse-carrier-error.md` 全文：实际空间／window 区别、完整逆与全区间量词。
- `joint-sonin-cross/general-finite-set-model-and-growth-fees.md` §§1–4：完整两残差、所有混合 delay、Aγ/Jγ/Cγ 的原证明。
- 571 §§1–3：同一 receiver pair、完整 J inverse、δ 的准确方向与反射。
- 572 §§4–7：coherent 后完整尾、moving-exponent PNT/Abel、严格 Γ 端点和相位运输。
- 557 §§1–6及542／555相应对象和来源入口：最强旧 whole leading 4/5 的具体短链。

本审没有重证532所继承的实位 Sonin 来源、经典 PNT/Mertens 或MV外部原定理，
没有外网检索／数值截断；这些依赖按已消费资产使用，新增消费方向在下面独立检查。

## 2. 原域、全部 signed interval 和 clipping

H=L²(R,dy)，实际空间为 Ran P_M，window 为 P_TH；两个压缩 G_M、G_T 的逆仅在各自空间使用。
B/D 有界可逆，z=S_Tw∈P_TH，y=P_Mz∈Ran P_M，故候选在实际完整变分原域内。
此合法性不证明 y 是原 Weil du／Dlog 源的像，报告没有偷换该角色。

对完整 D/D* 每对正 delay a,b，三项的公共相位确为 e^{-iR(a−b)}。
bulk 支撑 J0=(0,T)∩(a−b,T+a−b)，两剪切为 J0∩{y<a}、J0∩{y>T−b}。
所以 a+b<T 时剩正区间 (a,T−b)，a+b>T 时只剩两剪切交叠的负区间；等号为零。
全部 paired 级数总绝对质量≤(Σn^{-1/2})²=m^{-2}，每个区间长≤T，故在 H 中绝对收敛。
这同时支付了所有尾和有界算子交换，不是假设有限 word 的绝对 Neumann 和收敛。
B、W 后字母质量至多 Mm^{-2}、M²m^{-2}，所以可合法套532的 ALL-J 量词。

Pk=k 给 ⟨k,Pz⟩=⟨k,z⟩；写 h=y−z，实际 clipping 差精确为

    e_clip=2 Re⟨k−w,z⟩−2 Re⟨Bz,Bh⟩−||Bh||²。

因此主报告(4)三项费用准确，没有交换 P_M 与 B。
实际权乘 |b|²≤M² 后，在 R≥exp(16e^L) 甚至每个固定正 θ 的相应高层都由 R^{-1/4}
胜过全部 exp(O(e^L/L)) 常数。这个部分仅是旧 clipping 在明确候选上的直接推论。

## 3. 两完整平方及实际残差方向

正 Gram 的精确变分恒等式分别给 D_T=q_T−V_T(z)≥0、D_M=q_M−V_M(y)≥0，故

    q_M=q_T−D_T+e_clip+D_M=s_T+δ_win−D_T+e_clip+D_M。

主报告(2)的正负号正确。只丢正 D_M 只能给 actual q_M 下界，不能给所需误差上界。
三稿中 r_T/r_M 有整体相反的记号习惯，但每份内部的差式及平方一致；不构成语义依赖变化。
按主报告的正残差约定，在同一 ambient H 中确实有

    r_M−r_T=(P_M−P_T)Wz+P_MW(y−z)−(k−w)。

第一项可用 Wz 的完整 carrier 字母质量；后项用原有界 W，而非错误交换投影。
所得 h_R≤e_R(1+2M²/m²) 和 D_M≤m^{-2}(M√D_T+h_R)² 正确。
两个平方都付后，主报告(6)才是合法双向绝对运输，未把模型 δ_+ 当成 D_T。

## 4. 完整缺陷的投影身份、相位与真实 tail

560精确 residual 给 r_T=P_TWq，q=H_+Dv+L_-D*u，v=L_-D*w、u=H_+Dw。
B P_TH 闭且其正交投影为 B P_T G_T^{-1}P_T B*；因此

    D_T=||Π_(BP_TH) Bq||²≤M²||q||²
       ≤M² τ_F(T)² (||v||²+||u||²)。

最后一步是两个外半线支撑正交且 delay≤T 的 cross-window 压缩为零。
τ 是全部 n 的完整尾，不留下第二条未付尾；此处只用 operator 上界乘真实 v/u，
没有把全 H 的任意输入下界指派为 receiver 的实际费用。

J^{-1} 表示与此 residual 重组完全兼容，所有 returns 仍在完整 Gram 中。
分别 clean V=bar b·v、U=b·u 时 C_b=diag(1,bar b/b)，J_b=C_b*JC_b，
其 off-diagonal 是 (bar b/b)K；defect 稿(5)连同 E* 的相位亦正确。
反射给 ||u||=||v||，未将两边界独立丢弃。

## 5. 固定安全16的全部费用和 uniform 量词

F_L={p<e^{2L}}、E_L=e^L/L、γ=log4/(2L)，取 L 充分大使0<γ<1/2。
572已付的紧参数 PNT/Abel可直接用于权1 Euler partition；二次 remainder O(log L)
及最终 s>1/3 的更高阶可和项均为 o(E_L)。所以

    log M=(1+o1)E_L，log m^{-1}=(1+o1)E_L，log Aγ=(4+o1)E_L。

完整 T=Γ(R)，起点 |R|=exp(16e^L) 给 γT=(8log4+o1)E_L。
令 d0=8log4−4>7，τ≤exp[−(d0+o1)E_L]。
用560旧原 residual 与 coercivity，确得

    |b|²D_T≤4M⁶m^{-4} τ² T/(2π)，         指数10−2d0<0；
    |b|²D_M的最坏tail指数≤14−2d0<0；
    |b|²|δ_win|≤2M⁴m^{-3} τ T/(2π)，    指数7−d0<0。

不能先套较弱 ||S−G_T^{-1}|| 再多损一次 M，忽视旧精确 residual；报告已扣除这个更强旧推论。
572均值经投影 identity 也能支付同一层的 D_T、D_M，是合法但非必要的另一条上界。
没有以此声称572整个 θ>2e 范围已运输，也没有用充分证书失败证明实际 lower。

560模型全部常数须一并付。其 Cγ 的四块指数为7、7、10、11；Jγ 多出的 moment
只有 log 为 O(L) 的量，不改4E_L主项。因8log4>11，完整 model/arithmetic tail同样衰减。
S_T原pair费用是该完整逆常数的子上界，故对 e_S 使用 Cγ 是合法较大估计。
乘 (1+T) 的费用 logT 在起点是 O(L)。起点后 T e^{-γT}、T e^{-2γT}递减，
√T R^{-1/4}也递减；Γ在充分大正R单调、负频由实结构和Γ偶性运输。
所以结论确为 ALL |R|≥exp(16e^L) 的统一界，而非只在一个短区间平均：

    sup |ε_(F_L)(R)| ≤ exp(−c e^L/L) →0，某固定c>0。

ε在这里是真实 2πρ−Γ+全部prime powers 的完整误差，不是δ_win。
Γ只在估计中用渐近，finite Euler μ不替代−ζ′/ζ；本门未增加pole矩消失条件，双pole完整保留。

## 6. 原源费用、强旧与停止决定

单位 Fourier 乘子压缩给 K_hi=1_I F_unit* M_(1_hi ε) F_unit1_I，
故 ||K_hi||_(du→du)≤sup_hi|ε|=η_L→0。未归一 hat 的型积分需1/(2π)，
但该因子已在 Plancherel 中，算子界不能重复除2π。主报告(9)正确。
这对ALL原complex L²源的高频误差部件有效，因而限制到Dlog源仍是型界；
没有证明 K_hi 保持Dlog图域，也没有把 Fourier 切片误称同一compact源。
完整 K 尚有全部低频／核心，不能由本界删去；高度平均本身也不支付与任意 |rhat|² 的相关费用。

本门相对原稿完成了实际候选的 cofinal 安全高层消费，但依赖链只有
532 ALL-J → 完整 signed carrier → 两变分平方/旧560 residual → 已付PNT尾 → 原乘子高频部件。
没有新的独立算术／几何容量。最强旧542全k/band＋555完整prime row经557给whole leading4/5；
本安全层远高于其有利高频尺度，未改变该预算、θ≤1危险核心、低频/coupling或通常Ξ门。
因此0新增数学轮和不建C036的归属准确，Goal完成门仍open。

停止范围不扩大为方法类不可能：source-adapted、Γ-relative、paid nonfinite compact、
新的全逆组织或真实global section/kernel/乘法＋独立局部消失／height/RR预算仍是合法逃逸。
但必须有新的同源对象和费用才重准入，不能把未知全Gram正性／容量当成新的假设名称。

## 7. 绑定版本

以下为本终审实际消费的四文件规范LF SHA256；hash只绑定版本，不代上述证明。

    goals/reviews/2026-10-20-actual-variational-sonin-transport-admission.md
      5841f47c22ef65272c842a69ffd83bc21046b0eea7c64ce5d7e2615f0f8a3615
    reviews/2026-10-20/variational-admission/candidate-domain-and-clipping.md
      b829b359f15ba3976fbe6e92afdaeb26f192470b9a1ca62cefb08f32f15feb16
    reviews/2026-10-20/variational-admission/full-defect-and-receiver-control.md
      c9a64851735c0ef3aa7b660ce4203e9f4d08504b81147faae58bfb712c42efdf
    reviews/2026-10-20/variational-admission/actual-source-norm-and-sign-audit.md
      7248218fcaf6906032ba34eb69d344af7eca076565517173dc201a6d8e85bfaf

无阻塞修订；后续任何语义／范围更改应重核受影响消费。此稿不认证root结算、远端同步或运行Goal状态。
