# C054 root实际定量推导：待独立proof/root消费

2026-10-29；非已结算结论。此推导是上轮准入止后新形成的actual量化第一步。固定对象/源见C054；不使用未证uniform Cauchy界或fullgap Ω符号。

令μ=dt/(2π)，actualΠ核为K，j(t,s)=|K(t,s)|²。对R=Π，E_X(f)=1/2∬|f(t)−f(s)|²j dμdμ。一般0≤R≤Π的quasi-free covariance，需独立核E_R=同jump+∫|f|²κ_R dμ，其中κ_R=K_R(t,t)−K_R²(t,t)≥0。

固定ψ、g=ψ*ψ#，G=|ψhat|²，a=1/2。G≥0，G≤1，|t|≤1时G≥cos²(1/16)>1/2。定义

    A_R=E_R(e^(-iat)G)−E_R(G)
       =∬(1−cos a(t−s))G(t)G(s)j_R(t,s)dμdμ≥0。

Killing项在此差中exact取消。对δ∈(0,1]，按near |t|≤δ、far |t|>δ分三种：

* NN：tGt−sGs=t(Gt−Gs)+(t−s)Gs，故平方≤2δ²|Gt−Gs|²+4(t−s)²GtGs；因为ratio≤2且1−cos a(t−s)≥a²(t−s)²/4，第二项≤16/a²倍anomaly integrand。
* NF/FN：选near坐标作第一个t，|t−s|≤2|s_far|，平方≤2δ²|Gt−Gs|²+8s_far²G(s_far)²。
* FF：平方≤2t²Gt²+2s²Gs²，可用8倍两far项统一支配。

合并后先积分row而不分别重复估tail，得到jump部分

    E_jump(tG)≤2δ²E_jump(G)+8/a² A_R
                    +8∫far t²G²K_R²(t,t)dμ。

一般R的near killing≤δ²E_kill(G)，far killing≤∫far t²G²κ_Rdμ，所以总式仍为

    V_R[g′]≤2δ²V_R[g]+32 A_R+8 B_R(δ)，
    B_R(δ)=∫far t²G²K_R(t,t)dμ≤B_Π(δ)。

这是实际同receiver的joint不等式；tail未证前仍conditional。另一proof腿须由旧C052 allfixedB局部化及全线(Tail)证明B_Π→0：T=(logX)^4，Gevrey2上界付far √X加权尾绝对0，δ..T exponential diagonal付middle绝对0。不能只用旧相对o(√X/log²X)。

若该tail闭，令q0=完整Q(g)=完整Q(τ_a g)，q1=完整Q(g′)>0。平移相等须保indefinitepole Lorentz boost与Γ/pp；537付三固定源合法正性。取

    δ=min(1/2,sqrt(q1/[16(q0+1)]))，
    ε=min(1/2,q1/260)>0。

当B_Π≤q1/64且三误差均≤ε时，Vg≤q0+1、0≤A≤2ε、Vg′≥q1−ε，故

    q1−ε≤q1/8+64ε+q1/8=q1/4+64ε，

而65ε≤q1/4矛盾。于是所有common R≤Π都有同组三fixedtest max误差>ε，X0独立R。δ只是证明cutoff，不改ψ/g/a或实际规则；不让δ随X/测试源移动。

候选扩展：若正外部scale β_X或多个positive covariance相加，同不等式逐项/乘β仍成立，但tail变为相同加权tail。只有加权tail→0才可继承结论；无界gain可能破坏此前提，保合法未排，不把原Π的tail界免费套过去。主合同不优化gain，不据此缩小长期Goal。
