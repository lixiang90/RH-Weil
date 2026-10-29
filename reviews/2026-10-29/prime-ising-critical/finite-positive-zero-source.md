# 有限非等权铁磁零点：自含单位圆盘证明与来源范围

2026-10-29。关闭admission中有限Lee–Yang必要依赖；以下是经典有限图机制的自含special-case证明，不主张首创，也不消费未读的Lieb–Sokal正文。仅限有限scalar Ising、非负实pair耦合及沿同一复参数的正实磁场权，足够当前实际family。

## 1. 来源取得与准确限制

已查到Lieb–Sokal1981原书目/DOI10.1007/BF01213009，publisher给CMP80,153–179及摘要。Project Euclid页面为service/security notice，Springer为subscription preview；通过10808获取的公开download端点返回HTTP200但只有1162-byte HTML，非PDF。签名验证失败即停止，未保存冒充PDF的文件、没有原论文页/定理/证明被读。作者页另返回502，不继续纸链。

下述正性不依赖摘要推断原假设，也不按uniform-field theorem直接替代不等权磁场。它直接证明本模型所需有限命题。经典背景只作bibliographic context，外部作者的general theorem仍未审。

## 2. 二变量收缩引理

设multiaffine多项式P(x,y;v)=A(v)+B(v)x+C(v)y+D(v)xy对全部|x|,|y|,|v_j|<1非零。固定其余v于开圆盘，A≠0。对角P(t,t;v)=A+(B+C)t+Dt²在|t|<1无零。

若D≠0，其两个根（保重数）的模都≥1，根积A/D遂满足|A/D|≥1；若degree降为1或0则D=0。因此收缩

    C_xy P(z;v)=A(v)+D(v)z

对|z|,|v_j|<1仍非零。D=0时由A≠0直接成立。引理只用二次根积，不用未核的一般Asano定理。其他变量仍multiaffine，所以可逐次应用。

## 3. 每条铁磁边的圆盘稳定性

有限无loop图G=(V,E)，J_e≥0有限。令t_e=exp(−2J_e)∈(0,1]，为边两端分配独立half-edge变量x_(v,e)。边多项式

    P_e(x,y)=1+t_e(x+y)+xy。

若0<t<1，解为y=−(1+tx)/(t+x)，且

    |1+tx|²−|t+x|²=(1−t²)(1−|x|²)>0。

所以|x|<1时任何根y的模>1；若t+x=0，P_e=1−t²≠0。t=1时P_e=(1+x)(1+y)，同样在开bidisk非零。各边乘积因而在所有half-edge变量的开圆盘中非零。

在每个vertex把其incident half-edge变量用§2逐对收缩，保留all-unselected或all-selected单项式，删去不一致的partial选择。每次仍multiaffine/stable，最终每顶点只有一个z_v。Degree0顶点另乘1+z_v。结果为

    P_G((z_v))=Σ_(σ∈{±1}^V) exp[Σ_e J_e(σ_vσ_w−1)]
                                  ∏_(v:σ_v=−1) z_v。

这项展开由每边same-spin系数1、opposite-spin系数t_e和每顶点收缩的一致性逐项核出，不是假设spin模型与多项式相等。故P_G在全部|z_v|<1非零。

## 4. 非等权磁场与当前素数源

给任意正实c_v和复z，令h_v=c_v z。有限partition function满足精确等式

    Σ_σ exp[Σ_e J_eσ_vσ_w+Σ_v h_vσ_v]
       =exp[Σ_eJ_e+Σ_vh_v] P_G((exp(−2h_v)))。

Re z>0时所有fugacity模<1，故非零；spinflip给Z(−z)=Z(z)，遂Re z<0也非零。Z是非零实系数偶整函数，全部零点（含重数）只能在imaginary axis。任意固定有限正权、任意图、J=0边均已覆盖，不要求权相等、整数或有理数。

本候选M²/(2B)=Σ_vw_v²/(2B)+Σ_(v<w)(w_vw_w/B)σ_vσ_w。B>0、a>0时J_vw=w_vw_w/B≥0、c_v=w_v/a>0；常数self项及Z(0)正归一化不改变零点。因此当前实际Z_X,λ满足上述结论，没有取任何未知ζ零点位置，也没有把abstractpositive cone membership作为假设。

有限指数和为exponential type；本页只付其有限正零轴，未自动付全部零谱求和/统一tail/D′极限或Weil身份。那些前件仍由两独立原稿及不同fresh/root核。边多项式/经典引理是当前family证明的一部分，不另计数学轮，不开启图/J/磁场参数续造。
