# 一次同对象trial预算：强旧lower保留，相关包络不足

2026-10-27；`/root/one_trial_engine`独占执行稿。按README／STATE、check→show、当前Goal／C046历史结算、D20261027H、宏观前沿及[冻结准入](next-one-trial-budget-admission.md)恢复。本次只读既存n／c2／prime-root／d/u有理证书，没有重跑c2、旧projection scalar或G，不更换h0/F8/cutoff，不调t／prime／Chebyshev，不修改STATE／cadence／看板／文献库。

## 1. 实际执行与结果

执行：

```
python scripts/tf_reader_one_trial_budget.py
```

已terminal exit0，约0.0079秒。正式原件为[脚本](../../../scripts/tf_reader_one_trial_budget.py)与[one-trial-budget.json](one-trial-budget.json)。全部接受运算都是exact Fraction在已认证有理端点上的加乘除／max／min，平方根仍由原p^−1/2有理witness给出并重新核p·low²≤1≤p·high²。浮点仅作打印，不参与接受。

| 量 | 显示值 | 消费意义 |
|---|---:|---|
| a2 | 约0.28181361751725 | 新c2读出的p2能量 |
| drest·a2的lower | 约0.00051666323928845 | 弱于旧n²，不能改称新whole lower |
| 旧n²的lower | 约0.02266102783295458 | combined a lower仍取它 |
| combined a upper | 约17.984178804052817 | 新p2/rest upper小于旧u·n upper |
| 固定J区间 | 约[0.00109891438836745,0.00161824390692015] | 已合法付费的非零scalar trial区间 |
| residual²充分上界 | 约0.15041395135671254 | 远未达d_lo/32 |
| d_lo/32 | 约4.914894986912351·10^−6 | 原reserved residual门 |
| 免费知道exact a时，该symbol包络最优值的lower | 约0.05383265720924377 | 仍为reserved门约10952.96倍；不是actual residual下界 |

当前residual包络上界为reserved门约30603.70倍。J半宽≤1/128通过，但原残差门不通过。源有理区间和所有exact接受bool／版本在JSON；本表小数不是正式端点。

固定variational读出与旧谱下界／新Cauchy下界相交后，短向外略化为

\[
 q_0\in[0.001260053521478990,\ 1].
\]

正式lower约0.001260053521478991，优于旧coarse lower约0.0008094495577533444；宽仍约0.9987399465，**原宽≤1/16未通过**。此固定单项lower改善与whole残差瓶颈分开报告，不作经典全源／成长／whole4/5UPPER新后果。

## 2. 对象与强旧扣除

同一physical H=L²(R+,dx)，h0=1_[1,2]、norm1，B为原F8的有限commuting-unitary dilation乘积，P是原Sonin正交投影，v=P B h0。n=||v||²、c2=<v,U_log2v>均来自实际证书；G=P W P|RanP，W=B*B，a=<v,Gv>=<v,Wv>，b=||Gv||²。当前输入实，linear-first内积；没有把原五源allcomplex责任缩成实域命题。

令W2=(3/2)I−(U_log2+U_-log2)/sqrt2，Wrest为其余七prime因子。W2与Wrest在整个H上相交换且正，故

\[
 a_2=\tfrac32n-\sqrt2c_2,
 \qquad d_{rest}a_2\le a\le u_{rest}a_2.
\]

这不需要假设G或P与每个dilation交换；只是v∈RanP令全W的二次型等于G的二次型。七因子drest/urest用原sqrt witnesses exact向外相乘，sqrt2=2·(1/sqrt2)亦不另引浮点。

更强旧source身份为

\[
 n=\langle v,Bh_0\rangle=\langle B^*v,h_0\rangle,
 \quad a=\|Bv\|^2=\|B^*v\|^2\ge n^2.
\]

B normal来自有限commuting-unitary因子。因此实际combined lower取max(n_lo²,d_lo·n_lo,drest_lo·a2_lo)，upper取min(u_hi·n_hi,urest_hi·a2_hi)。本次lower准确仍取n_lo²，新p2 lower对这一强旧没有净改善；upper确有固定数值作用，不能反向称c2完全无用。上下界与source角色均保留，未以较弱子界的改善替whole净值。

## 3. 非零trial、相关残差与包络诊断

冻结t=1/u_hi、z=t v。这个非零scalar trial是同一真实Hilbert向量的倍数，未改为存储的t v*；输入n/c2也都已指actual v。若未来实际执行改用t v*，相应J／残差还需另付δv运输，不能借本记录免付。本次**已经**给出z=t v的有向J和true-H residual充分上界，不能继续沿用“没有任何非零trial／J”的旧阶段描述；没有执行的是Gv、actual residual值或足够紧的b/a。

\[
 J=2tn-t^2a,
 \qquad r^2=\|v-Gz\|^2=n-2ta+t^2b,
 \quad b\le u_{hi}a.
\]

保留这条相关性后，在0≤t≤2/u_hi有

\[
 r^2\le n_{hi}+(u_{hi}t^2-2t)a_{lo}.
\]

该有向包络的最优t正为冻结的1/u_hi，给本次上界n_hi−a_lo/u_hi。不把a,b拆成无关rectangle，也没有为了通过门去调t。合法variational界为q0∈[J_lo,J_hi+r²_hi/d_lo]∩[0,1]。程序再与旧n_lo/u_hi以及Cauchy n_lo²/a_hi lower相交；后者利用新的a upper而改善单项q0 lower，仍未达到宽门。

若免费知道actual a,n，而仍仅用b≤u_hi a，最小化的同一symbol包络是n−a/u_hi。由本次已认证a_hi,n_lo，其数值必≥n_lo−a_hi/u_hi，后者仍大于d_lo/32。这里的“必≥”仅指这个**充分包络的最优值**，不是actual r²；不能由此排一般trial或实际b计算。这定位到需要更紧的同向b/a／actual residual费用，而不是继续改善弱a lower。

## 4. 停止与净范围

本冻结预算已耗用，结果为不足。按原门停止此输入／b≤u a标量包络的自动续算，不调t、继续prime／degree／Krylov或重展示抽象收敛式。真正有费的global mixed／远尾／actual b信息、不同trial或独立算术源保持合法，须新input/test/net准入；本结果不证明这些方法不可能。

同一物理对象、输入n/c2量词及全Hilbert误差角色没有扩张。没有T/E/cross／Hfin、经典all-source／成长signed、primitive整过滤／mixedRR或Ξ结果；Γ/contact/properpowers/双pole及原du/Dlog仍归原目标。最强经典542+555→557 whole leading4/5负惯性UPPER未改。标准既有不等式的固定有理预算比较为0数学轮，不建C047/584，也不完成或blocked长期Goal。

本分支只保存独占三个文件，交root/fresh消费当前版本；没有外部文献检索／PDF下载、Git提交或root状态变更。独立审核、strongest-old最终归属和每轮同步由root统一处理。
