# C002 候选审查：反向核不能由背景作统一相对下包

2026-10-13。独立审查主代理提出的候选；本文件不改 C001、STATE 或 cadence，
不启动新合同。恢复时已读 AGENTS/README/STATE，运行 check/show，
STATE 尚为 C001 reviewing；另核读当前 Goal、C001、D20261013。
实际工作树含 C001 新审查与主代理脚本；本审查只写此独立输出，无后台进程。

结论：候选在以下精确辅助核量词下成立，未发现代数或量词反例。
这是一条可由主代理复核消费的解析证明，不是新数值样本或完整 Weil 正性边界。

## 1. 对象与准确结论

固定 `L=log13`，使用 `scripts/qw_matrix.py` 的真实来源符号：
`H_P(n,m)=w02(n,-m)`、`H_A(n,m)=-w_real(n,-m)`、
`H_R(n,m)=-w_primes(n,-m)`，`H_BG=H_P+H_A`，`n,m>=1`。
这里 R 的负素数分布号已经吸收到 H 的 sine 公式中。

待消费的准确命题是

\[
\forall C\in\mathbb R\quad\forall M_0\in\mathbb N\quad
\exists M\ge M_0:\quad
v_M^T(H_R+C H_{BG})v_M<0,
\qquad v_M=e_M-e_{M+1}.
\tag{1}
\]

所以不存在固定有限 C 对所有实有限支持正指标向量成立
`h_R>=-C h_BG`。等价地，在有限支持向量上
`inf h_R/h_BG=-infinity`；分母严格正由 C001 背景 Gram 得出。
v_M 的范数是 sqrt2；正规化将两种能量同除2，不影响(1)或比值。
对每个固定 N，H_BG 严格正，始终可找依赖 N 的有限 C_N；
被排除的是固定 L 的所有 N 共同常数，不能把(1)改成固定 N 内任意大 C。

## 2. 背景上界：全 M 明确常数

复用 C001 已独立推导的真实 Gram 表达。令
`kappa=2pi/L`、`x=kappa M`、`y=kappa(M+1)`，
`t_j=2j+1/2`、`c_j=1-exp(-t_j L)`、
`gamma=8sinh²(L/4)/L`。在单参数通道定义

\[
r_t(z)=\frac{t}{t^2+z^2},\qquad s_t(z)=\frac{z}{t^2+z^2}.
\]

则精确地

\[
h_A(v_M)=\frac2L\sum_{j\ge0}c_j
 \{[r_{t_j}(x)-r_{t_j}(y)]^2+[s_{t_j}(x)-s_{t_j}(y)]^2\},
\tag{2}
\]

极点 h_P 为同一个花括号在 `t=1/2` 乘 gamma。
对 `M>=1`，`y<=2x`。在 `z in[x,y]` 上

\[
|r_t'(z)|=\frac{2tz}{(t^2+z^2)^2}
 \le\frac{4tx}{(t^2+x^2)^2},
\quad
|s_t'(z)|=\frac{|t^2-z^2|}{(t^2+z^2)^2}
 \le\frac1{t^2+x^2}.
\]

间隔 `y-x=kappa`，故由均值定理与
`t²x²/(t²+x²)²<=1/4` 得

\[
|\Delta r|^2+|\Delta s|^2
 \le\frac{5\kappa^2}{(t^2+x^2)^2}.
\tag{3}
\]

函数 `(t²+x²)^-2` 对 t>=0 单调下降；步长2积分比较给

\[
\sum_{j\ge0}(t_j^2+x^2)^{-2}
 \le x^{-4}+\frac12\int_0^\infty(t^2+x^2)^{-2}dt
 =x^{-4}+\frac\pi{8x^3}.
\]

因 `0<c_j<1`，全 M>=1 有明确上界

\[
0<h_A(v_M)\le\frac{10}L
 \left(\kappa^{-2}M^{-4}+\frac\pi{8\kappa}M^{-3}\right),
\quad 0\le h_P(v_M)\le5\gamma\kappa^{-2}M^{-4}.
\tag{4}
\]

从而 `h_BG(v_M)<=K_BG M^-3`，可取

\[
K_{BG}=\frac{10}L\left(\kappa^{-2}+\frac\pi{8\kappa}\right)
 +5\gamma\kappa^{-2}<\infty.
\tag{5}
\]

此直接全域通道上界也验证主代理的低/高 t 分段 O_L(M^-3)，
无需样本、渐近未定项或扩大任何数值矩阵。

## 3. 真实素数来源的准确主项及统一余项

有效原子为
`K={2,3,4,5,7,8,9,11}`，`w_k=Lambda(k)/sqrt(k)>0`，
`theta_k=2pi log(k)/log13 in(0,2pi)`。
endpoint13 的 sine 为零，保留或删去对本反向核等价。
单原子反向核是

\[
H_{R,k}(n,m)=\frac{w_k}{\pi(n+m)}
 [\sin(n\theta_k)+\sin(m\theta_k)].
\]

用两条 diagonal 与 off-diagonal 直接相减，严格给

\[
h_R(v_M)=\sum_{k\in K}\frac{w_k}{\pi(2M+1)}
 \left[\frac{\sin(M\theta_k)}M
 -\frac{\sin((M+1)\theta_k)}{M+1}\right].
\tag{6}
\]

所以令
`T_M=sum_k w_k[sin(M theta_k)-sin((M+1)theta_k)]`，
`W=sum_k w_k`，可写为

\[
h_R(v_M)=\frac{T_M}{2\pi M^2}+E_M,
\qquad |E_M|\le\frac{W}{\pi M^3}\quad(M\ge1).
\tag{7}
\]

余项常数核查：第一个 sine 系数与 `1/(2M²)` 的误差
是 `1/[2M²(2M+1)]<=1/(4M³)`；第二个的误差
是 `(3M+1)/[2M²(M+1)(2M+1)]<=3/(4M³)`。
因此(7)含实际所有素数幂，主系数没有漏2或改变负号。

## 4. Cesaro 矩与负子序列：不需要频率有理独立

写

\[
T_M=\sum_{k\in K} A_k\cos[(M+\tfrac12)\theta_k],
\qquad A_k=-2w_k\sin(\theta_k/2)\ne0.
\]

频率无0，且在 mod 2pi 意义下无相等或相反碰撞：
`theta_k-theta_l=0 mod2pi` 因二者同在(0,2pi)只能给 k=l；
`theta_k+theta_l=0 mod2pi` 只能给 `kl=13`，
而有效整数 k,l>1 均小于13，13素性排除该等式。
其和在(0,4pi)，故无需检查额外的整数倍。
特别 `2theta_k=0 mod2pi` 会给 k²=13，亦不可能。

对任一 `omega!=0 mod2pi`，有限几何和除长度趋0；
用一次指数展开及二次乘积公式，即得严格 Cesaro 极限

\[
\frac1Q\sum_{M=1}^Q T_M\to0,
\qquad
\frac1Q\sum_{M=1}^Q T_M^2\to S
 =\frac12\sum_k A_k^2
 =2\sum_k w_k^2\sin^2(\theta_k/2)>0.
\tag{8}
\]

这只要求有限频率无上述碰撞，不要求 theta_k/pi 无理，
不使用 Kronecker、素数定理或任何 ζ 零点输入。

补足“bounded implies infinitely negative”的量化：
取 `B=sum_k|A_k|>0`，则 `|T_M|<=B`，且
`T_M²<=B|T_M|`。因此

\[
\liminf_Q\frac1Q\sum_{M=1}^Q (T_M)_-
 =\liminf_Q\frac1{2Q}\sum(|T_M|-T_M)
 \ge\frac{S}{2B}.
\]

选 `c=S/(4B)>0`。若仅有限 M 有 `T_M<-c`，
则负部 Cesaro 上极限至多 c，与上述严格冲突。
更强地，该集合下密度至少 `S/(4B²)>0`，因为
`(T_M)_-<=c+B*1_{T_M<-c}`。
所以存在任意大的 M，使 `T_M<-c`。
同理也有正子序列；本候选只消费负子序列。

## 5. 量词闭合与逃逸范围

对任意固定有限实 C，设 `C_+=max(C,0)`。
由(5)(7)，负子序列上

\[
h_R+C h_{BG}
 <-\frac{c}{2\pi M^2}
 +\frac{W/\pi+C_+K_{BG}}{M^3}.
\]

选该子序列上的
`M>(2pi/c)(W/pi+C_+K_BG)` 且 `M>=M0`，右侧负，
即证(1)。从同式与背景严格正还得该子序列上
`h_R/h_BG` 无下界。这里没有交换增长 L 与 Fourier cutoff 极限：
L 永远固定为 log13。

**非重复016。** 016 BE 排除的是全 Weil P−V 分解中指定
逐块绝对范数步骤，并在 lambda→infinity 得到线性 degree 损失。
本候选保留真实 signed atoms，在固定 lambda=sqrt13、M→infinity，
排除辅助反向指标核的 `H_R>=-C H_BG` 常数类。
二者对象、极限与估计方法不同；无需重复016作为本证明。

**不得越界的结论。** 正指标反向核 H 不是完整 W，
其负方向不是完整 Weil 型负方向，也不是奇 O 的底态。
这里未控制同号指标块、常数模耦合或完整联合能量。
实际 h_R 沿此子序列绝对值趋0，而比值发散；
含任意固定正的质量项 `epsilon||v||²` 的估计不被此反例自动排除。
依赖 N 的费用、有限指定低谱空间、相消后的完整源耦合、
另一个提供同阶 M^-2 coercivity 的背景都属于未被排除的逃逸条件。

**相对长期 Goal。** 这可停止一类自然辅助来源估计，
但还不能宣称实际完整核心问题的实质方法类已被排除。
没有新增完整算术正性、RH、simple-even 或增长支集证书。
背景优势必须接回完整对象才可能改变宏观瓶颈；目前该瓶颈不变。

本审查没有运行新的谱样本、计算零点或调用数值证书。
指定旧件/关键词检索未见同一固定 L 相对反向核结论；
没有全文复审全部笔记，不声明外部新颖性或世界优先权。

停止／重新准入条件：若候选只停在(1)，停止统一背景相对下界技巧；
重新准入需要限制空间的独立依据、允许并支付明确质量费用、
或实际完整联合核中可证明的不同 coercivity。不要加大样本来回避(1)。
唯一下一动作：主代理独立复核(3)(6)(8)和明确对象后，再决定该限定边界
是否值得登记为 C002 的结算证据；本子审查不自行消费轮数或改合同。
