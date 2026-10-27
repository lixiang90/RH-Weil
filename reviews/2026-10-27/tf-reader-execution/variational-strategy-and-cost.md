# 固定 q0：有向变换、已执行成本和实际低区间标量

2026-10-27，`/root/q0_variational`独占稿；供root／fresh消费。不改STATE、cadence、文献库，不建C047／584，不换h0、F或五源参数。恢复已读README／STATE、check→show、Goal、D20261027F、宏观前沿及execution-handoff。完整五源T/E仍待交付；本文实际执行的是同一q0输入的成本证书和projected-input norm，**没有通过q0宽≤1/16验收**。

## 1. 避免第一次无界尾操作的同一对象恒等式

H=L²(R_+,dx)，F是核2cos(2πxy)的自伴酉，P是cutoff1 Sonin投影。M=RanP在F下不变，故FPF=P。B为冻结八个素数的有限Euler乘积，FBF=B*；B/B*相交换，所以W=B*B满足FWF=W，G=(PWP)|M及其逆也与F交换。因此

\[
 F\Pi_FF=B^*PG^{-1}PB,\quad
 q_0=\langle PBh_0,G^{-1}PBh_0\rangle,
 \qquad h_0=1_{[1,2]}.
\]

这与保存的v0=PB*Fh0同值，二者由F酉运输；没有更换physical输入或reader目标。新写法先作用有限B，再做P，避免一开始就在Fh0的无限物理尾上应用所有负dilations。

令N_F=9699690。实际finite step为

\[
 f=Bh_0=\sum_{d\mid N_F}\frac{\mu(d)}d1_{[d,2d]}.
\]

256是相加step数，不是互不交的partition cell数。`tf_reader_q0_cost_certificate.py`实际用整数端点sweep和独立pair-overlap双和两种exact rational方法核得

\[
 \|f\|^2=\frac{19189712}{4849845}
 \in[3.956768102898133857886179,\ 3.956768102898133857886180].
\]

canonical非零partition有382个cells。这个数是||Bh0||²，绝不能直接称||PBh0||²；后者在§3另算。

## 2. 已实际运行的充分成本证书

[脚本](../../../scripts/tf_reader_q0_cost_certificate.py)与[JSON](variational-cost-certificate.json)使用整数平方根给每个p^−1/2有理上下界，再向外定点幂／binary search核实真实残差的充分包络。m=∏(1−p^−1/2)、M=∏(1+p^−1/2)、d=m²、u=M²的区间均保留原件，rho_interval已明确包实际rho，不只包其上端。

若按全谱Neumann，exact residual满足||r_n||²≤rho^(2n)||v||²≤rho^(2n)||f||²。脚本为final d/32门预留action误差，先令该包络≤d_lo/128，得到首个通过**该充分测试**的n为4,429,773。

Chebyshev residual可用

\[
 p_n(\lambda)=\frac{T_n((c-\lambda)/a)}{T_n(c/a)},
 \quad c=(M_{hi}^2+m_{lo}^2)/2,
 \quad a=(M_{hi}^2-m_{lo}^2)/2,
\]
\[
 \|p_n(G)v\|\le2\left(\frac{M_{hi}-m_{lo}}{M_{hi}+m_{lo}}\right)^n\|v\|.
\]

因为p_n(0)=1，(1−p_n(G))/G是degree n−1的polynomial trial，不是假装求得了G逆。脚本对4||f||²q^(2n)≤d_lo/128认证n=4,451。对exact reference始终在M的组织，含初始P共4,452次P；每P按双cutoff两次F共8,904次cosine action，W按八个三项因子组织对应71,216次dilation（另有初始B）。P_N不是投影，实际误差实现不能未经付款保持RanM；这些只是exact reference上的primitive计数。

上述次数不是必须执行的最少次数，不是actual q0难度下界，也不否定更好trial／Lanczos／source-adapted组织。它们已经把此前“有限可算”收缩为具体成本，说明直接无压缩逐word展开不适合作为默认实现；尚未付每次F／P的实际成本和最终J误差，不能据计数宣称q0已算。

脚本还实际给了z=0的合法全Hilbert variational证书：J=0、||r||²=||v||²≤||f||²，投影上界相交后只有q0∈[0,1]。它明确不通过1/16，不能把它称为成功的q0 reader。

## 3. 实际实施的低区间标量，避开无穷物理grid

root指定进一步实施[低区间脚本](../../../scripts/tf_reader_lowband_step.py)，实际输出[lowband-step-certificate.json](lowband-step-certificate.json)。一次运行41.99秒，exec session32360已terminal exit0，不留后台程序。它没有执行百万次operator迭代，而用同一个f的低forcing g=LFf：

\[
 \|Pf\|^2=\|f\|^2-\langle g,R_0g\rangle,
 \quad R_0=(I-C_0^2)^{-1},\quad C_0=LFL.
\]

把Ff写成384个integer-frequency endpoint项

\[
 (Ff)(y)=\sum_u\tau_u\frac{\sin(2\pi u y)}{\pi y},\quad
 \sum_u\tau_u=0,\quad N_F\tau_u\in\mathbb Z.
\]

为避免大J差和||f||²−||g||²的消去，使用

\[
 T(n)=2\pi n\left(\frac\pi2-\operatorname{Si}(2\pi n)\right),
 \quad T(0):=0,
\]
\[
 \|1_{(1,\infty)}Ff\|^2
 =\frac1{2\pi^2}\sum_{u,v}\tau_u\tau_v
       [T(u+v)-T(|u-v|)].
\]

这里的T(0)=0与T(x)=2πx(π/2−Si(2πx))的连续延拓相容；例如∫_1^∞cos(0)/y²dy=1应按1−T(0)读取。端点整数的sin/cos值精确，使该公式与全physical Fourier tail一致，未用有限域matrix residual。把频率先用整数权聚合后实际计算68,037个非零frequency。

对n≥40，T(n)的等价Laplace表达为T(n)=∫_0^∞e^−v/[1+(v/(2πn))²]dv。几何有限和给精确余项符号和上界(2K)!/(2πn)^(2K)，不是把发散asymptotic级数无条件取极限。对n<40，用有理π midpoint处的Si Taylor，逐项向外定点运算及real Taylor余项；actualπ引起的argument误差另用|Si′|≤1运输。260位向外定点工作精度，最大小n Taylor432项、Laplace88项，公式缓存68,038个值（含0）。

g的monomial moments也独立读取：moment0由Στ=0化为−Στ_u T(u)/(2π²u)；k≥1用integer-frequency exponential积分的精确recurrence，只有有限inverse-π powers，未在y=0做未经估计的oscillatory quadrature。

## 4. N26 polynomial trial的真实低Hilbert残差及R0运输

采用C_N的N=26 cosine Taylor，shifted Legendre basis L_l(x)=P_l(2x−1)、l=0,…,52，Gram为diag(1/(2l+1))。实际moments∫L_l x^n=(n!)²/[(n−l)!(n+l+1)!]。其矩阵与C_Ng全部以向外区间运算形成。

高精度mpmath solve只选择了一个明确有理coefficient trial y；接受依据是完整polynomial在L²(0,1)中的残差

\[
 r=C_Ng-(I-C_N^2)y.
\]

其norm按实际Legendre Gram逐项认证，不是只看mpmath solve残差。对x=C_Ng，

\[
 |\langle x,R_Nx\rangle-\langle x,y\rangle|
 \le\|R_N\|\|x\|\|r\|,
 \qquad R_N=(I-C_N^2)^{-1}.
\]

在polynomial正交补上R_N恰是I。全R0−R_N另由上一轮已认证的C0 gap及全kernel Taylor residual付款：

\[
 \|R_0-R_N\|\le M_0M_N\delta_N(\bar\kappa_0+\kappa_N),
 \quad |\langle g,(R_0-R_N)g\rangle|
       \le\|R_0-R_N\|\|f\|^2.
\]

这才允许低区间trial运输到真实P的全physical norm。实际polynomial残差平方上界约5.66·10^−205，trial二次误差约4.75·10^−98；主宽度来自全resolvent运输，上界约2.1664·10^−16。JSON中均保存有理原界，正文小数只是便于读数。

## 5. 实际结果和未通过的q0门

认证得到

\[
 \|PBh_0\|^2\in
 [0.15053580249546810381525278277638089497,
  0.15053580249546853709208093816137523167].
\]

该显示小数应理解为摘要；精确有向界由JSON的rational endpoints定义。低forcing norm²约3.7502924231，外部Ff tail²约0.2064756798，R_N correction约0.0559398773，与上式分账相容。

只用d/u谱界得到实际粗区间

\[
 q_0\in[0.0008094495577533444756\ldots,1].
\]

因此**q0宽≤1/16仍未通过**。没有实际构造full G非零trial，也没有full G的J／true-H residual验收，更未计算五源T/E或Hfin符号。低区间Pnorm是原q0 reader的一个实际组件，不能将它当作更容易的替代目标或整项q0数值。

若采用零trial并用本次更紧的Pvnorm残差上界，它仍只给宽区间；低区间证书不能免去关键full-inverse责任。可保的下一技术路线是对同一v的更好有限trial和真实G残差验收，而不是增加源模式、换F/L或再次展示抽象Neumann式。若root判定具体成本不支持，按保存stop规则记录此未通过状态，不升级为数学方法类不可能性。

本分支未改STATE／cadence／库；两脚本及JSON只是建设性执行证据，不自行计研究轮、重开旧合同或完成Goal。最终范围由root／fresh核实际版本后消费。

## 6. 一次实际G-action才可能改变当前停止判断

当前唯一尚有明确检验意义的固定一步是：保持v=PBh0，实际认证w=Gv及a=<v,w>、b=||w||²。连同本次已付n=||v||²，任一明确rational t给trial z=t v，

\[
 J(t)=2tn-t^2a,\qquad
 \|v-Gz\|^2=n-2ta+t^2b.
\]

可以预先固定选择规则为从认证n/a区间取一个有理midpoint t，再按上述真实残差及J误差验收原宽度门。若成功，只改变同一q0组件的可执行性；若实际残差仍大，停止这个冻结一维trial，不自动扩Krylov阶数或换输入。它不测试全五源Hfin或RH。

**在scalar阶段尚无这个action输入。** 原lowband脚本只认证有限step f的Pf norm；v自身有真实无限Fourier尾，并非该脚本的有限step输入。不能将已付scalar低moments／norm当成已实现Gv，也不能把a、b的抽象存在式宣布为新ready reader。原定停止判断限于这一阶段；下节记录root从已执行trial中发现并实际提取的analytic-vector输入，更新了“只有scalar”的输入状况，**full-G action仍未执行**。

## 7. 从实际trial提取的显式analytic vector（追加执行，非重跑scalar）

root指出现有witness保留了x=C_Ng及rational trial t，其低Hilbert残差e=x−(I−C_N²)t已实际认证。故可从同一证书提取

\[
 \ell=R_0g,\qquad
 \ell_{app}=g+C_Nt,\quad
 \|\ell-\ell_{app}\|
 \le\eta_R\|g\|+\kappa_NM_N\|e\|.
\]

这是R_Ng=g+C_NR_NC_Ng的直接恒等式，不是对未构造Gv的假设。`tf_reader_lowband_vector.py`已实际运行，读取原scalar／gap证书，不重跑Si、scalar或G。它选取旧trial区间的确切rational midpoint（本次所有旧trial区间实际均为singleton），旧residual enclosure仍覆盖该选择。

脚本从t的Legendre coefficients重构C_Nt的27个even-monomial coefficient区间，再取确切rational midpoint polynomial p_star。其误差按全L²(0,1)界δ_poly≤Σcoefficient半宽另付；如此输出的是**确切有限analytic函数**，不只是一组不指定代表元的浮点系数：

\[
 \ell_* =1_{(0,1)}(g+p_*),\qquad
 v_* = f-1_{(1,\infty)}F\ell_*.
\]

384个g的integer-frequency项、27个p_star rational coefficients、同一f的256个step项均已保存于[lowband-vector-input.json](lowband-vector-input.json)。v_*的真实无限Fourier尾保留在这个解析定义中，没有先截成巨大physical grid。完整误差是

\[
 \|v-v_*\|\le
 \eta_R\sqrt{\|g\|^2_{hi}}+M_N\sqrt{\|e\|^2_{hi}}+\delta_{poly}
 <1.061\cdot10^{-16}.
\]

这里κ_N≤1仅作保守放大，M_N<10^6已从实际C0证书／δ_N核实；JSON保存各项有理上界及输入hash。F、H为contractions，所以ell误差原样传到整个physical Hilbert空间中的v误差。

该实际输入允许root对一个固定bounded action作有内容的下一准入：例如U_log2的误差transport保持δ_v，G的transport至多||G||δ_v，但**实际action值／tail quadrature／成本仍须另外执行与认证**。它没有给full-G的a、b、J或q0宽1/16，没有五源T/E；不能因向量已给就预填这些结果。它也不改变h0/F/L、source或长期Goal。新输入与§6的抽象a/b存在式不同，是否足以准入一次固定action由root消费实际版本后决定。
