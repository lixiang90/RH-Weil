# 实际加权链的新边：闭性方程、电荷自由度与全主关系检验

2026-10-22；本轮独占推导。恢复G20261014、0c4f固定基线、STATE/D20261022D及当前宏观前沿后，
仅检验432真实HH₁电荷的具体新边，不开新数学合同或改变轮数。本稿不修改公共状态。

## 1. 原域、闭性与原费用

沿430–432，令

\[
 A=\operatorname{alg}(1,u,u^*,D_{\rm src}),\quad
 Q=A/\mathcal S_1,\qquad q:A\to Q.
\]

原u是实际酉算子，\(A(h)=VU(h)V^*\)，\(\|V\|=\sqrt2\)。对物理源
\(r\in C_c^\infty((-L,L),\mathbf C)\)，置\(h_r(s)=r(-s)\)、\(F_r=A(h_r)\)。
这里U是原时间卷积，不是实际adelic DGA的Schwartz dilation lift。
全部算子都在原Hilbert空间，不能用商中符号代替原源范数。

\[
 \|F_r\|\le2\|r\|_1\le2\sqrt{2L}\|r\|_{du}
 \le2\sqrt{2L/\log2}\|r\|_{D\log}.                         \tag{1}
\]

最后只用本仓Dlog权至少log2；若采用553的Hlog规范，还多一个正的常数项，界仍有效。
这是F_r的原bounded算子费用，不是商的positive能量，更不是未给截面lift的费用。
对每个非零compact r，431的有限矩阵符号给

\[
 c_r=q(u^*)\otimes q(uF_r),\qquad
 b_1c_r=q(F_r-uF_ru^*)\ne0.                                \tag{2}
\]

所以432的\(\Omega\)仍不能作用于裸链。537的r₀是非零compact物理源，亦适用(2)。

## 2. 一个完全准入的闭修补，电荷却为零

不重复有限u轨道平均。直接加入另一条、腿次序不同的实际边：

\[
 d_r^0=-q(F_ru^*)\otimes q(u),\qquad z_r^0=c_r+d_r^0.
                                                                    \tag{3}
\]

\(b_1d_r^0=-q(F_r-uF_ru^*)\)，故z_r⁰确为Q上一循环。原有界提升已经严格满足

\[
 [u^*,uF_r]-[F_ru^*,u]=0,
 \qquad\boxed{\Omega(z_r^0)=0}.                            \tag{4}
\]

不是只在迹类商中抵消。标准二链边界还给

\[
 z_r^0=1\otimes q(F_r)-b_2\big(q(u^*)\otimes q(u)\otimes q(F_r)\big).
                                                                    \tag{5}
\]

因此它是424(18)在当前真实源域内的精确实现。单位测试链的电荷为零；
不声称\(1\otimes q(F_r)\)或z_r⁰的HH₁类本身为零，普遍微分也可能有非零HH₁类。
用原operator norm计算projective一链的代表费用
\(\|z_r^0\|_\pi\le2\|F_r\|\)，原费用完全可付；全源电荷却皆为零。
这里仅记原有界提升的projective代表费用，不宣称商完成下Ω连续或由此判定其Hausdorff性质。
就Ω数值而言，这会消关系，也会丢掉r₀，不能称为所求非退化regulator。

若只把d_r⁰改成对称交换子或内自同构的上述标准链同伦，(4)不改变。
这不排除带新算术数据的新边；只是该实际同lift修补本身没有新电荷。

## 3. 所有修补的自由度可精确定位

设另一个准入新边d_r满足\(b_1d_r=-b_1c_r\)。于是

\[
 \zeta_r=d_r-d_r^0\in Z_1(Q),\qquad
 \Omega(c_r+d_r)=\Omega(\zeta_r).                            \tag{6}
\]

反过来，任意\(\zeta_r\in Z_1(Q)\)都产生修补d_r=d_r⁰+ζ_r。
因此闭性方程给的是循环空间上的仿射集合：它不确定regulator的非零值。
取HH₁商后自由度同样是HH₁类；边界不改变Ω。
有一个独立自然的arithmetical ζ_r仍可能解决比较问题，但必须给来源和规范，不能由“已经闭合”推出。
这里不宣称所有自然选择不可能，也没有把432已有非零HH₁资产抹去。

## 4. 可完全计算的非零新边：通过非根和原费，失败全主关系

固定\(k\in C_c^\infty\)，原427/432已付

\[
 \zeta_{r,k}=q(A(h_r))\otimes q(A(k))\in Z_1(Q),
 \quad
 \Omega(\zeta_{r,k})=-4\int s\,r(-s)k(-s)ds
                  =4\int u\,r(u)k(u)du.                   \tag{7}
\]

把它加入(3)就得到确有非零电荷的实际闭修补，不需要新相对理想。
对537固定r₀取\(k(u)=u\overline{r_0(u)}\)，则

\[
 \Omega(\zeta_{r_0,k})=4\int u^2|r_0(u)|^2du>0.            \tag{8}
\]

原费用也明确：\(\|A(k)\|\le2\|k\|_1\)，
\(\|\zeta_{r,k}\|_\pi\le4\|k\|_1\sqrt{2L}\|r\|_{du}\)，且

\[
 |\Omega(\zeta_{r,k})|\le4\|uk\|_2\|r\|_{du}.             \tag{9}
\]

但它不能消405全部physical Pan。其唯一自然的标量延拓是全L²连续泛函
\(\ell_k(r)=4\int uk(u)r(u)du\)。405明确的非零物理关系P=Cp满足全部平移τ_aP仍为Pan；
553已付这些平移的线性span在原全线L²及Dlog图范数中稠密。
若ℓ_k消全部τ_aP，则连续性迫ℓ_k=0，即uk=0 a.e.；这与(8)矛盾。
所以存在一个实际主关系平移使该修补的电荷非零。

此处不擅自把S_exp非有限传播核算子放进430的有限传播原代数。
严格结论是：compact源的闭链已合法；若试图以保持(7)且对S_exp连续的方式扩域来做全关系测试，
标量公式必失败全Pan。若不扩域，则Pan∩C_c∞=0，关系检验为空，不能记为通过。
可用光滑cutoff crop任意固定P并在S_exp收敛，得到相同的强制标量延拓；
这仍不自动支付任意源族的一致cofinal费用。

还有更直接的正二次模型：令\(k_r(u)=u\overline{r(u)}\)，取ζ_(r,k_r)。所有compact源上

\[
 \Omega(\zeta_{r,k_r})=4\int u^2|r(u)|^2du\ge0,\quad
 \|\zeta_{r,k_r}\|_\pi\le8L^2\|r\|_{du}^2,
 \quad\Omega(\zeta_{r,k_r})\le4L^2\|r\|_{du}^2.             \tag{10}
\]

它保r₀、有真实正号和原du/Dlog费，但延拓到405非零P时严格为正，故同样失主关系。
因此真实HH₁电荷的非零、闭性及正二次读出，都不足以选出Weil型。
该旧端点电荷只看m(-∞)=0、m(+∞)=2；其公式不含完整有限素数幂、Γ或双极点。

## 5. 换相对理想时，432不能自动搬运

若选\(J\supset\mathcal S_1\)并使F_r−uF_ru*∈J，则裸c_r在A/J闭合。
这没有让它在Q=A/S₁闭合，不能直接代入432的Ω。
要复用ordinary-trace定义，须另给\(\tau_J:J\to\mathbf C\)，准确满足

\[
 \tau_J|_{\mathcal S_1}=\operatorname{Tr},\qquad
 \tau_J([A,J])=0.                                         \tag{11}
\]

这才保证换提升不改变\(\Omega_J(c)=\tau_J\sum[A_i,B_i]\)。仅有非紧δF∈J不支付(11)。
如果扩大到让全部旧A(h)也属于J，则(11)与427的非零
\(\operatorname{Tr}[A(h),A(k)]\)矛盾；这种全吞源理想不能承载保普通迹的标量regulator。
没有证明由δF生成的任意代数/闭理想必然吞掉全部源，因此不把这个条件障碍泛化为所有J不可能。
适当的更小理想、带取值module的trace、非局部/无限转移或新相对pair仍是合法方向；须给实际比较。

直接mapping cone若用同一链及其同一提升作相对边，其规范配对抵消，归424(5)–(9)。
要保非零值，须独立给出非exact的比较循环或规范迹类残差；(6)就是该剩余责任。
它不是由cone名称或idele fibre acyclicity自动产生的电荷。

## 6. 与全主关系、整模型及完整Weil预算的消费接口

所需新增输入可以精确表成一份实际数据，而非未知regulator名称：

1. 对物理S_exp源r及实际DGA的所有Pan同伦，给规范新边或实际J/相对pair；
   闭链类对全Pan为边界或准确principal变换，r₀及两个degree不被全消。
2. 同一算术整模型上，局部消失过滤在该映射下可定义，gluing boundary消失并有实际section lift；
   lift的原du/Dlog、Schwartz/cofinal及高度/分母费用分别给出。
3. 该同一对象的截面乘法及平方RR容量独立可证，再证明其finite与arch预算的总差等于完整Weil型。

已有真实P¹_Z二次容量或函数域C×C的RR，不付上述同源映射；但不能否认这些容量确实存在。
函数域正例额外有真实对应的composition/transpose、对角局部交数、有效截面乘法与Hodge/RR，
并保H⁰/H²全部pole贡献。连续±d控制已有闭/相对设施却有相反Weil号；(10)更说明
任意正端点读出可以在两类上都造出，未选择目标谱型。

经典消费始终保568的完整Γ/contact、全部\((p,k)\) prime powers和双pole。
405已付完整解析公式及Pan消失；不能把(7)/(10)的端点迹直接认作其中一个预算片再丢其余片。
允许跨位signed补偿、determinant-line/cocycle协同及强拓扑源族；只在独立证明同源预算身份后才能消费。
若按\(Q_W\)选ζ_r使Ω=Q_W，闭性当然可以额外修补，但这仍是把旧Weil型包装为HH₁读出，
不是独立有效性、RR容量或经典RH正性输入。

## 7. 本分支的准确结算

新增检验信息是：在真实源域里能给一个实际闭修补，也能通过另加旧cycle得到非零甚至positive二次读出，
但闭性留下的电荷自由度恰为HH₁循环；明确的原费非根候选失败405全关系。
这是424/427/432/553的直接合成与候选准入，不重计为新定理或新数学轮。
它没有解决同一整模型上的local filtration/section lift/primitive平方RR，未改strong-old
542+555→557 whole leading4/5上预算、actualcore/coupling/Ξ或长期Goal完成门。
停止同lift对称补边和任意固定probe附加cycle；下一需要实际算术新边来源及(11)或链比较，
或可独立付款的非局部/无限转移及完整全位预算身份。单独“新的相对边”或“已经闭合”不足以晋级。
