# C053辅助证明：两个固定flat bump的Fourier首项与共同good set

2026-10-28；`/root/post_quiet_phase_fresh`当前C053辅助proof任务，非旧准入fresh。已恢复README／STATE、check→show、AX、C053固定合同及当前前沿／总结。只证明合同两份固定bump的Fourier端点渐近与共同good-set费用；不处理实际Riesz G₂、不证明完整J_n^g下界或C053结论。无外部primary／PDF／web／query／数值／Git／STATE／cadence操作，不改g、δ、ψ或合同；所有工作仍属于同一次C053迭代，出稿不代root／最终fresh消费。

## 1. 固定对象与精确交付

对一个先固定λ>0和正normalization N_λ，定义

    f_λ(u)=N_λ exp[-1/(1−(u/λ)²)]， |u|<λ，外置0，
    F_λ(t)=∫f_λ(u)e^(−itu)du.

本合同只用这一定义的两个固定实例：g=f₁，N₁使||g||du=1；ψ=f_b，b=δ/2=log2/8，N_b使∫ψ=1。不是允许改变λ或选择更好bump的候选族。原Fourier没有1/√(2π)因子。

下文自含证明：存在T_λ、M_λ<∞，使全部t≥T_λ有

    F_λ(t)=K_λ t^(−3/4)e^(−√(λt))
                   [cos θ_λ(t)+R_λ(t)],                 (1)
    θ_λ(t)=λt−√(λt)−3π/8,
    |R_λ(t)|≤M_λ t^(−1/2),
    K_λ=2N_λ e^(−1/4)√π(λ/2)^(1/4)>0.

R_λ可取实值，因为f_λ实偶。该余项按leading envelope作**绝对**界，不是相对于cos值的误差；在cos零处不作虚假的相对下界。Phase有明确导数

    θ_λ′(t)=λ−√λ/(2√t)→λ>0,                            (2)

且t≥1/λ时λ/2≤θ_λ′≤λ。

## 2. 整个积分的合法轮廓变形，避免cutoff余项

先不乘N_λ，令B_λ(z)=exp[-1/(1−(z/λ)²)]。它在C除±λ外全纯。取一次fixed r₀∈(0,λ/8)，把原区间轮廓变为：

    −λ → −λ+e^(−iπ/4)r₀ → λ−e^(iπ/4)r₀ → λ.

中段是固定水平线，虚部−r₀/√2。端点用半径ε的小弧避开±λ：局部s到endpoint的扇区满足|arg s|≤π/4，Re[(λ/2)/s]≥λ/(2√2|s|)。因此弧上B_λ为O(exp(−c_λ/ε))，而e^(−itz)在下半平面t>0的模≤1；小弧积分趋0。Cauchy定理于是给原积分等于上述三段，未跨任何奇点。

水平中段B_λ在固定compact路径有界，故其积分为O_λ(exp(−h_λ t))，h_λ=r₀/√2>0。这比(1)所需的t^(−5/4)e^(−√(λt))更小。这里没有引入任意C∞ partition cutoff，因此也没有把mere superpolynomial Fourier误差误当比e^(−c√t)更小。

右端点写u=λ−s，a=λ/2。精确partial fraction为

    1/[1−(1−s/λ)²]=a/s+a/(2λ−s).

令A_λ(s)=exp[−a/(2λ−s)]。它在|s|<2λ解析，A_λ(0)=e^(−1/4)，且沿|s|≤r₀有

    |A_λ(s)|≤C_λ， |A_λ(s)−A_λ(0)|≤C_λ|s|.           (3)

右段方向从λ−e^(iπ/4)r₀到λ，故其贡献准确为

    I_R(t)=e^(−iλt)∫_0^(e^(iπ/4)r₀)
                          exp(−a/s+its)A_λ(s)ds.        (4)

左端点贡献为overline(I_R(t))：用u↦−overline(u)、实even的B_λ及相反端点方向可直接核。水平中段保上面的指数小界。

## 3. 端点积分精确化为Gaussian，再控制余项

设q=e^(−iπ/4)，τ=√(at)，d=√(a/t)=a/τ。先取s=e^(iπ/4)r，再令r=d v，则

    −a/s+its=−qτ(v+v^(−1)),
    I_R=e^(−iλt)e^(iπ/4)d
        ∫_0^(r₀/d) exp[−qτ(v+v^(−1))]
                                A_λ(e^(iπ/4)dv)dv.      (5)

对v>0作实变量变换

    y=√v−1/√v， v+v^(−1)=2+y²,
    v(y)=[(y+√(y²+4))/2]²,
    J(y)=dv/dy=2v(y)^(3/2)/(1+v(y)).

这是(0,∞)到R的递增diffeomorphism。J(0)=1、J′(0)=1；当|y|≤1时

    J(y)=1+y+O(y²),                                    (6)

并且全real y有v(y)≤C(1+|y|)²、J(y)≤C(1+|y|)。这些直接由上面的v公式得到：y≤0时v≤1，y≥0时√v≤y+1。

令Y_τ=√(r₀/d)−√(d/r₀)→+∞。将(5)写成

    I_R=e^(−iλt)e^(iπ/4)d e^(−2qτ) L_τ,
    L_τ=∫_(−∞)^Yτ e^(−qτy²)
                       A_λ(e^(iπ/4)d v(y))J(y)dy.      (7)

因为Re q=1/√2>0，所有以下估计均为绝对收敛。由(3)及vJ的多项式上界，替换A_λ为A_λ(0)的误差至多

    C_λ d∫_R e^(−(Re q)τy²)(1+|y|)³dy
       =O_λ(d τ^(−1/2))=O_λ(τ^(−3/2)).                (8)

这里只在y≤Y_τ时使用A_λ，因而其argument始终在合法射线段|s|≤r₀。A替换后，J的全线多项式界使上端截断Y_τ≥1的尾为O_λ(exp(−cτ))。由(6)，近|y|≤1的J−1−y贡献是O(∫y²e^(−cτy²)dy)=O(τ^(−3/2))；远区只给指数小项。奇函数y的全线Gaussian积分为0。因此

    L_τ=A_λ(0)∫_R e^(−qτy²)dy+O_λ(τ^(−3/2))
       =e^(−1/4)√π(qτ)^(−1/2)+O_λ(τ^(−3/2)).          (9)

末个complex Gaussian公式自含成立：对real positive参数由平方积分的极坐标计算得到；两侧在Re z>0解析，identity theorem给∫e^(−zy²)dy=√π z^(−1/2)，取正real处为正的branch。此处q^(−1/2)=e^(iπ/8)，没有额外branch或π常数。

将(9)代回(7)，用d τ^(−1/2)=a^(1/4)t^(−3/4)及−2qτ=−√(λt)+i√(λt)，得

    I_R=e^(−1/4)√π a^(1/4)t^(−3/4)e^(−√(λt))
          ·exp[i(−λt+√(λt)+3π/8)]
          +O_λ(t^(−5/4)e^(−√(λt))).                    (10)

取两个端点的2Re，再乘N_λ并吸收水平中段指数小项，即为(1)。所有误差常数仅依这个fixed λ／normalization／r₀，独立t、n和后续good-set选择。

## 4. 每个[n²,n²+L₀]的坏集界，无相位独立假设

取任意fixed L₀>0、0<ε≤1/2，记I_n=[n²,n²+L₀]。对n²≥1/λ，定义

    B_(λ,n)(ε)={t∈I_n: |cos θ_λ(t)|<ε}.

在phase变量中，|cos θ|<ε每个π-period占长2arcsinε≤4ε；θ_λ(I_n)长度≤λL₀，相交period数≤λL₀/π+2。Inverse phase derivative≤2/λ，故明确有

    |B_(λ,n)(ε)|≤(8/π)εL₀+16ε/λ
                  ≤3εL₀+8/λ.                          (11)

这是对所有充分大n的统一Lebesgue测度界，不仅某条子列；可再与trivial L₀上界取min。它具有要求的CεL₀+C/λ形式，实际上保留更强的ε/λ endpoint项。

当n≥2M_λ/ε且n²≥T_λ，(1)余项全段≤ε/2。因此在I_n\B_(λ,n)(ε)上

    |F_λ(t)|≥(K_λε/2)t^(−3/4)e^(−√(λt)).               (12)

这里bad set只按leading cos定义；余项没有在cos零处被除掉。无Diophantine或两个相位独立前提。

## 5. 固定g、ψ的共同good set及可复用平均lower

令λ₁=1、λ₂=b=log2/8，取一次0<ε≤1/48和任意fixed

    L₀≥64(1/λ₁+1/λ₂).

定义E_n=I_n\(B_(λ₁,n)(ε)∪B_(λ₂,n)(ε))。由(11)的较粗末式及union bound，

    |I_n\E_n|≤6εL₀+8(1/λ₁+1/λ₂)≤L₀/4,
    |E_n|≥3L₀/4.                                      (13)

该结论对全部n≥某fixed N成立，N只依两个固定bump、ε／L₀。E_n上两个(12)同时成立，故

    |ghat(t) ψhat(t)|²
       ≥[K₁² K_b² ε⁴/16] t^(−3)
                       exp[−2(1+√b)√t].               (14)

特别地，t≤n²+L₀、√t≤n+√L₀，(13)–(14)给只涉及两个bump的平均lower

    ∫_(E_n)|ghat(t)ψhat(t)|²dt
                      ≥c_(ε,L₀) n^(−6)e^(−C_b n),     (15)

其中c_(ε,L₀)>0、C_b=2(1+√b)，均先fixed。这个平均没有包含G₂，不能冒作完整moment下界。

供主作者交集使用的准确接口是：若同一I_n上另有actual Riesz坏集C_n且|C_n|≤L₀/4，则|E_n\C_n|≥L₀/2，且(14)在该交集原样保留。没有假设G₂相位与两个bump独立，没有证明actual Riesz幅度／解析边界、其C_n测度或其余项。那些仍由主proof在原对象上支付；本稿不能据(15)把一个可能在E_n上小的未知G₂当有正lower。

## 6. 消费范围

本稿证明了固定g／ψ的endpoint leading非零、absolute envelope remainder、phase导数和全大n共同good-set／双bump平均lower。若主稿采用不同的同对象物理边界证明，可以不消费本Fourier支撑；不得因本稿存在便宣称完整J_n^g、inverse-Euler ratio或C053已经闭合。

没有新primary或未读asymptotic引用；以上来自完整轮廓、精确Gaussian变量替换及elementary测度估计。Norm／Fourier与合同固定一致。它只是同一C053的一份辅助原件，不新增轮／预算／counter，不操作Goal、STATE或Git；最终独立审者和root须按actual消费链对齐是否使用、原件版本及仍未付Riesz部分。
