# 固定 fractional-part 两源核：cotangent／joint 旧范围比较

2026-10-29；独占旧去重。已恢复README／STATE、check→show、同Goal／C053／D20261028AZ／formal18及宏观前沿。锚为 `0/history54/latest590/formal18`，同1793085111 Goal open。本稿只核087–097及10-28 coprime-additive-input四原件，不授C054／数学／来源预算，不改STATE、cadence或看板。

**结论：固定核的正 Gram、双源性及非零混合 dilation，不能作为新 joint 核心输入。087已经有同一 fractional-part 临界线 Gram；089–092已有 determinant／cotangent／paired-DFT组织。当前没有新增 mixed RR、完整Γ／primepowers／双pole身份或原norm下独立有利净估计。另须冻结091 shared-gcd筛的一项过宽前件，见§4；不将它继续当成无条件已付。**

## 1. 当前核与087的实际同源关系

固定题给
\[
 h(u)=e^{-u/2}\{e^u\},\quad Jr=h*r,\quad
 B(r,s)=\int\widehat r\,\overline{\widehat s}\,
 m(t)\frac{dt}{2\pi},\qquad
 m(t)=\frac{|\zeta(1/2+it)|^2}{1/4+t^2}.
\]
原du、Fourier `rhat(t)=∫r(u)e^{-itu}du`、第一槽linear不变。h两端分别受 `e^{u/2}`／`e^{-u/2}` 控制，故h∈L¹∩L²，J是实际L²卷积算子，`|B(r,s)|≤||h||₁²||r||₂||s||₂`；双Dlog费用除以log2。它是合法正型对象，不是尚待造的Hilbert空间。

087 QP式(12)已给真实 Nyman features `ρ_n(x)={1/(nx)}` 的
\[
 W_{jk}=\int |\zeta(1/2+it)|^2
 Q_j(1/2+it)\overline{Q_k(1/2+it)}
 \frac{dt}{2\pi(1/4+t^2)}.
\]
精确坐标为酉变换 `Uf(u)=e^{-u/2}f(e^{-u})`：
`Uρ_n=n^{-1/2}T_{log n}h`。因此当前卷积是这个实际feature族的连续源组织，不是首次出现两槽Gram。离散系数作该比较时是有限原子合成；不把δ标签冒作当前smooth/L²源。

标准独立平移差本来就有
\[
 B((T_a-I)r,(T_b-I)s)=\int\widehat r\overline{\widehat s}
 (e^{-ita}-1)(e^{itb}-1)m(t)\frac{dt}{2\pi}.
\]
mixed非零只说明既有Gram方向不正交，不提供prime交数、关系下降或signed相消。带标量dilation须保原标量，非零仍不是目标身份。

## 2. cotangent、gcd和Gram已付到哪里

| 旧原件 | 已付内容 | 不能由此消费的加强 |
|---|---|---|
| 087–088 | 实际finite positive Gram、完整affine constrained projection、Feshbach gain；local/parabolic/far各PSD，同一向量的exact能量分解、far periodic Loewner majorant | finite可解／正性／capacity单调不证明cofinal Nyman距离消失；不能忽略base coupling或只控制某一块 |
| 089–090 | cross-conductor `hr′−h′r=Δ` 的精确signed核；gcd/lcm、primitive harmonic的有限Möbius筛、solution-line cotangent和Type-I/II坐标 | cotangent闭式与有限重排不付增长determinant窗的Möbius bilinear净界；不能逐项绝对值后声称相消仍在 |
| 091–092 | coprime `(a,b)` 的reciprocity pair、一致kernel界、有限cotangent DFT及product-modulus差分，shared筛可按**实际**允许集作有限Fourier拆分 | 单项DFT系数有约√q费用；分开两个大cotangent再引用DFI/BC不自动付短Δ、移动moduli、outer Möbius、separation和全部dyadic总费。091密度／even-g须携§4限制 |
| 093–094 | logarithmic Riesz及local-Euler-removal bounds；endpoint weighted Riesz接口；093 SK的`δ=±1` principal平均保留 | 不付growing-δ、nonprincipal或canonical cofinal界；093 SL／094 SP任意fixed-D整定理消费按§4冻结待重闭 |
| 095–097 | response-aligned leverage、完整affine coupling、response rank-one anchor精确不改normalized方向；local+parabolic exact jump Gram和far-completed有限证书 | capacity／correction energy单独不能控endpoint Riesz norm；finite矩阵显式、positive或far费小均不证明所需统一渐近 |

087的optimizer实际含 `η=Q*(z+Gb)`：`α*=−W⁻¹η+(t+D*W⁻¹η)W⁻¹D/C`，其中 `C=D*W⁻¹D`。095–097继续要求定向 `EW⁻¹D/C`、`EW⁻¹η`及hard/easy泄漏，而不是只看Gram正号或增加方向数。这些是已有“response／coupling”责任，不能因当前核有mixed dilation便宣布已经支付。

本范围已有cotangent算术和真实Nyman Gram，未给“Vasyunin结构→经典mixed RR”定理；不新增Vasyunin闭式引用。

## 3. 10-28互素加法首门不能遗漏，也不能错套

其冻结规则用 `x=a/c` 进入log平移两源 `J_x`，按同分母减均匀项。已闭合
\[
 E_c(F)=\sum_{d\mid c}\mu(d)R_{c/d}(F),\quad
 R_1(F)=-\int F,
\]
以及同product cutoff、log d、剔除c=1的corner和global H¹绝对收敛。极限准确为
\[
 C_\infty=A_1/\zeta(2)+\zeta'(2)A_0/\zeta(2)^2
                  +\int_0^1\ell(x)J_x\,dx.
\]
grid泛函仍依赖两源，非两个常数型；该门未消费C∞非零。旧 `h/r` 是Fourier频率，`a/c` 是log平移实参数，当前h卷积亦不逐式等于C∞。

可继承的是**责任比较**：新mixed写法、含加法的整数参数、finite ratio原子及赋值的log-linear收缩，均未自动给完整Γ/contact／Λ(p^k)=logp／双pole。其root已按H¹ norm极限、共同crop和既有405／553／537闭合full-reader身份门；不是要求每层精确消Pan，也不是凭有限spurious原子判D′极限失败。当前h的global L²费更不能被称为逃出全部有限Sobolev连续责任的新机制；若只承担某个未来总型的一项有界补正，须另给实际无界腿及其完整mixed身份，不能把该未知背景算作已付。

## 4. 必须隔离的旧筛前件

091 RT把 `r=ga,r′=gb` 的解写为 `h_t=h₀+at,h′_t=h′₀+bt`，在p|g处断言两个禁残基总不同，并推出even-g全灭及RV密度 `∏(1−2/p)`。现文仅有 `(δ,ab)=1`，不足以排除p|δ。**这些宽句及依赖它们的任意δ消费须冻结。**

固定符号反例已足：`g=2,a=3,b=5,δ=2`，取 `h₀=h′₀=1`，则 `5h−3h′=2`，原 `r=6,r′=10` 且h=h′=1都primitive；t mod2的允许集为 `{0}`，非空。两个禁残基在此重合。此处不运行helper／数值，不把root拟存的helper结果提前当已核。

保留090 exact divisor-sieve、091按实际T_g的有限cotangent／Fourier恒等式；`(δ,g)=1` 子域才可沿用两不同禁残基及其density/even-g论证。`δ=±1`自动满足前件，093 SK此子域不回滚；094独立Riesz／Euler-removal、095–097线性代数不受影响。但093 SL／094 SP陈述含任意fixed-D，**整定理当前消费仍冻结待必要重闭**，不把“fixed-D可修”当已复核整链。本稿不展开root提示的loss修补或复跑helper；纠错原件与fresh/root重闭另办。

## 5. 此次准入净值

不否认h的实际正核、非零mixed响应或已有cotangent设施；它们已属于旧fractional-part／Nyman正Gram机制。`|ζ|²/|s|²` 的乘积相关谱也不是完整Weil的线性log-derivative身份；不能在critical line作未付绝对Euler展开，把相关项称为已恢复全部primepowers／Γ／poles。

没有新same-primitive source-map、principal／整截面／mixed RR，或signed/corecross独立原费净量，故该说法不通过新joint准入。不泛排fractional-part／nonlocal／relative／joint修复，不推Q负/RH反例。Whole4/5仅UPPER、关键箭头未变；本稿0数学轮，不给参数／candidate／source后继。

## 核读绑定

全文核087–097及coprime目录的candidate、source-norm、coefficient-fiber、root-consumption四原件；不扩外部引文或其它旧proof。全部按CRLF→LF计字节。关键绑定：087 `9015/847eedfd…`；091 `8812/00e9ab74…`；092 `12036/81437015…`；097 `7443/d891d172…`；coprime norm `10494/2639c943…`、coefficient `11239/b3088d51…`、root receipt `9405/8e71e381…`。按087→097再上述四原件顺序，将每条 `repo-relative-path<TAB>LF-bytes<TAB>full-sha256<LF>` 串接，其15项binding SHA256为 `500a1c1ffe3647c459e756b65c65e47d962919143bde6ced3a686fff62b14eaf`。未编辑这些旧件或消耗其旧next。
