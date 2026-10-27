# 固定c2的前四项：exact endpoint积分与实际认证

2026-10-27；`/root/c2_mixed_terms`独占稿。已恢复README/STATE、check→show、Goal、D20261027G、宏观前沿及固定pair门。输入严格为现存[显式向量](../tf-reader-execution/lowband-vector-input.json)，不重跑旧scalar或G，不改h0/F8/cutoff/五源半窗，不自行改STATE/cadence或计轮。

## 1. 实际输出与边界

脚本为[scripts/tf_reader_c2_mixed_terms.py](../../../scripts/tf_reader_c2_mixed_terms.py)，实际命令：

```
python scripts/tf_reader_c2_mixed_terms.py --output reviews/2026-10-27/tf-reader-c2/mixed-terms.json
```

exec session16438实际terminal exit0，约33.05秒；[JSON](mixed-terms.json)保存正式有理区间。180位向外fixed-point算术、Q余项目标10^−60，实际使用148715个不同Q值（含0），small Si Taylor最多396项、Laplace最多29项。显示值不是认证依据：

| 项 | 显示值 | 正式有理区间宽度的显示 |
|---|---:|---:|
| <f,Uf> | −0.2883680173314208 | 2·10^−180 |
| <ell*,FHcut U^−1 f> | −0.21432708798806835 | 5.58·10^−59 |
| <ell*,FHcut U f> | −0.19492157425883638 | 4.63·10^−59 |
| <ell*,U^−1 ell*> | 3.5373752771557125 | 9.91·10^−59 |

程序以exact comparison核全部四项宽≤1/16384。root须按+−−+合成，再减独立第五项，并支付v到v*的输入运输。这里没有完整c2结论，也没有G action、q0/J/residual或T/E结论。

## 2. 对象与dilation方向

physical H=L²(R+,dx)，F核2cos(2πxy)，Hcut=1_(1,∞)，U=U_log2，Uf(x)=2^−1/2 f(x/2)。NF=9699690，f=Σ_(d|NF)μ(d)/d·1_[d,2d]，g(y)=Στ_u sin(2πuy)/(πy)，ell*=1_(0,1)(g+p*)。τ_u以common NF整数numerator保存，p*的27个even系数为上一证书选择的确切有理数。实输入与实内积范围明示，不替原五源全complex责任。

实际

\[
 Uf=2^{-1/2}\sum_d\frac{\mu(d)}d1_{[2d,4d]},
\quad
 Hcut U^{-1}f=2^{1/2}\sum_{d>1}\frac{\mu(d)}d
                 1_{[\max(1,d/2),d]}.
\]

d=1的左移step落在[1/2,1]，highclip后为空；不可保留这个项。Uf的支撑本来≥2，所以Hcut不再删。截后endpoint sums分别384与383项。F作用finite step准确变为端点sin/(πy)的差；sqrt2／inverse sqrt2统一在每项末端乘，来自isqrt的有理包围。

<f,Uf>用全部256²个step overlap exact求和，未乘inverse sqrt2前为−3955669/9699690。端点是物理x值，不是source logtime，原h0 norm1未更改。

## 3. sine product的精确积分

R=1或1/2，a,b>0且2Ra、2Rb为整数。记

\[
 Q(k)=\pi k\left(\frac\pi2-\operatorname{Si}(\pi k)\right),
 \quad Q(0)=0,\quad k_\pm=2R|a\pm b|.
\]

分部积分给

\[
 J(c)=\int_0^R\frac{1-\cos(cy)}{y^2}dy
     =\frac{\cos(cR)-1}{R}+c\operatorname{Si}(cR).
\]

sin×sin化差后，k+与k−同parity，cos差准确为0；因此

\[
 I_R(a,b)=\int_0^R\frac{\sin(2\pi ay)\sin(2\pi by)}{\pi^2 y^2}dy
 =\min(a,b)+\frac{Q(k_-)-Q(k_+)}{2\pi^2R}.
\]

这保留了积分到0的可去奇点，也保留完整physical Fourier尾通过Plancherel/cutoff运输后的贡献。程序用twice-frequency整数key、common NF系数先exact聚合min项和Q权；cross-down147072 pairs聚合103484非零频率，cross-up与compact各147456 pairs聚合103837频率。没有oscillatory grid或未付款数值积分。

half-integer频率不能直接照抄旧T(n)的正号。现有DLMF公式输入只复用[前轮已库记录](../tf-reader-execution/dlmf-si-source-read-record.json)。在k≥80，实际Q为

\[
 Q(k)=(-1)^k\int_0^\infty
       \frac{e^{-s}}{1+(s/(\pi k))^2}\,ds.
\]

有限几何恒等式给K项后余项符号(−1)^K、大小≤(2K)!/(πk)^(2K)，随后再乘parity(−1)^k。k<80使用有理π midpoint的Si Taylor；integrated real sine Taylor remainder逐项取真实上界，actual π argument误差用|Si′|≤1另付。全部fixed-point乘除向外舍入；π仍是已认证Machin有理包围，不以floating sin/Si作证明。脚本与JSON均明确Q(0)=0。

## 4. polynomial cross及compact dilation

定义

\[
 M_j(a,R)=\int_0^R y^{2j-1}\frac{\sin(2\pi ay)}\pi dy.
\]

j=0时M0=Si(πk)/π=1/2−Q(k)/(π²k)，k=2aR。j≥1用I_n=∫0^R y^n sin(2πay)dy的odd递推：

\[
 I_1=-\frac{R(-1)^k}{2\pi a},\quad
 I_n=-\frac{R^n(-1)^k}{2\pi a}
      -\frac{n(n-1)}{(2\pi a)^2}I_{n-2},\quad n=3,5,\ldots.
\]

实际M_j=I_(2j−1)/π。这是exact endpoint recurrence，递推可能放大区间宽度，程序保全部向外区间并在最终真实标量宽度验收，不借浮点conditioning猜测。p*系数不再近似或重选。

第四项支撑0..1/2，且

\[
 \langle\ell_*,U^{-1}\ell_*\rangle
 =\sqrt2\int_0^{1/2}[g(y)+p_*(y)][g(2y)+p_*(2y)]dy.
\]

g(2y)=1/2 Στ_u sin(4πuy)/(πy)，所以g×g2及p×g2各付额外1/2；p*(2y)的j项系数为4^j a_j。p×p2用全部27²个monomial exact积分，其余三项用上述I_R／M_j。所有factor、radius和方向均保存在代码及ledger，不把第四项当同一norm。

## 5. 消费范围

输入版本、依赖interval脚本及本脚本LF SHA已嵌JSON。正式结果是四个已执行有理区间；本次时长不作复杂度定理。没有原源／成长量词扩张，也没有full-G或经典signed净后果；complete Γ/contact、properpowers、双pole、原du/Dlog及五源cross责任仍由原目标承担。

这里仅交root合成与fresh逆审。旧scalar／旧R0证书未重跑，未自行提交Git或修改看板/文献库；未声明新数学轮、C047/584或长期Goal完成。新外部来源未检索，DLMF仅复用此前已核四式；该标准实现不作为新算术输入。
