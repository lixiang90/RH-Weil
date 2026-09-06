# 320. 增长分离簇的共同正则化：以最大簇质量控制全部测试方向

2026-09-06，phase 3第4轮。[T/R，已通过独立内部复核] 完整实际算子的条件性集体预算。
簇存在、外部分离为[C/O]；不证明RH、全局正性或零点比例改进。

## 1. 定理对象、日程及结论

保持317的同一实际前缀、全部正负列、原始重数和sharp MT窗。
固定0<s<d0<1/2，0<theta<1，
k=max(s,1/4+Phi_s(theta)/2)<d0，L=log T，D=T^theta。
选择M>=1个互不相交深点簇Cj：所有簇内点深度>s；每簇有目标dj>=d0；
直径均<=r；每簇与该簇之外的所有深度>s的点距离至少D。
记c=Ar->0，目标高度在(0,T]，故M<=1+T/D。大T时r<=D/4。

Q=[hj/sqrt(Hj)]；Wj=sum_{w in Cj}2mw Hw；
Wmax=max_j Wj，Wtotal=sum_jWj。二者由原始列计算，不从原负谱反造。
令
\[
 \tau_T=c+L/D,\qquad
 \boxed{\lambda_T=L^4T^k+\sqrt{\tau_T}\,W_{\max}},\qquad
 R=\lambda_T(P+\lambda_T I)^{-1}.                         \tag{1}
\]
整个配置只使用这一个lambda和R。下文证明
\[
 \boxed{\operatorname{tr}(R\mathsf A R)_-
          \ge(a_s-o(1))W_{\rm total},\qquad
         \lambda_T/\|P\|\longrightarrow0.}                \tag{2}
\]
误差常数与M、重数及簇质量不平衡无关，只依赖固定参数和计数常数。
没有要求M有界；所有o(1)沿指定c(T)->0、T->infinity成立。
这里a_s是316的固定正相关常数，不是1，也不是全部负谱质量比例。

## 2. 选中正簇的块范数

记C为所有选中簇之并，omega_w=2mw Gw，S_j=sum_{Cj}omega_w，
Smax=max_jS_j。固定深度下大T时Hw<=Gw<=2Hw，故
Wj<=Sj<=2Wj。令B_C的列为sqrt(omega_w) gw/sqrt(Gw)，P_C=B_CB_C*。

同簇归一化gg内积绝对值<=1。不同簇的gg内积由317-(1)控制。
目标中心按高度排序；若w属于Cl、w'属于Cj，l!=j，则
|yw-yw'|>=D|l-j|-2r>=D|l-j|/2。
用319§2的Schur检验（行列权均sqrt(omega_w)）得
\[
 \|P_C\|=\|B_C^*B_C\|
 \le S_{\max}\{1+C_s(1+\log M)/D\}.                        \tag{3}
\]
具体地，每个权后行和为sum_{w'}omega_w' |corr_gg(w,w')|；
本簇至多S_l，其他簇至多C Smax sum_{j!=l}(D|j-l|)^-1。
因此控制量是最大簇质量，不是所有簇质量之和。

## 3. 正簇作用在全部负测试列上的共同界

分解K=B_C*Q=K_near+K_cross，K_near只保留w与目标j属于同一簇的条目。
偶性及sin相位给|K_wj|<=c sqrt(omega_w)，故各列非零行互不相交，
\[
 \|K_{\rm near}\|\le c\sqrt{S_{\max}}.                     \tag{4}
\]
其他条目用gh归一化远界。取Schur权pi=sqrt(omega_i)、qj=1，
a_wj为对应条目绝对值的支配界。准确的归一化行列条件为
\[
 \sup_w p_w^{-1}\sum_j a_{wj}q_j\le C(1+\log M)/D,\qquad
 \sup_j q_j^{-1}\sum_w a_{wj}p_w\le C S_{\max}(1+\log M)/D.
\]
因此
\[
 \|K_{\rm cross}\|\le C\sqrt{S_{\max}}\,(1+\log M)/D.
\]
结合(3)，大T时
\[
 \boxed{\|P_CQ\|\le C_s W_{\max}(c+L/D)
                        =C_s W_{\max}\tau_T.}             \tag{5}
\]
这里没有先把簇内所有小列误差独立相加；(4)依赖明确的不同行支撑结构，
(3)及跨簇Schur界才处理不同簇间的相关性。
即使c=0也保留跨簇项L/D；tau_T>0，所以(1)无零除问题。

## 4. 完整正背景与同一个逆变换

将全部P写成P_R+P_s+P_C+P_F：临界线、深度<=s非实点、选中深簇、其他深非实点。
分解穷尽所有正列，且每个F点距所有选中目标>=D，满足319的共同筛选。
由312／313，||P_R+P_s||<=C L(1+T^s)。
317给||Q||<=sqrt(1+epsilon_T)，epsilon_T<=C L/D。
再合并319-(7)和(5)，得到
\[
 \|PQ\|\le C\{LT^s+L^{5/2}T^{1/4+\Phi_s(\theta)/2}
                      +W_{\max}\tau_T\}.                 \tag{6}
\]
不是用全局||P||直接替代该定向合成范数。

令V=R^-1 Q=Q+PQ/lambda_T。由(1)、(6)
\[
 \|V\|\le\sqrt{1+\epsilon_T}
                 +C(L^{-3/2}+\sqrt{\tau_T})=1+o(1).       \tag{7}
\]
对任意a，R^-1>=I给||Va||>=||Qa||，但这里只需(7)的上界，
不依赖逐列误差推出矩阵误差的错误蕴含。

更完整地，令delta_T=||PQ||/lambda_T。展开V*V且使用317-(2)的原始Gram界，给
\[
 \|V^*V-I\|
 \le\epsilon_T+2\sqrt{1+\epsilon_T}\,\delta_T+\delta_T^2=o(1).
 \tag{7a}
\]
其中所用原始Gram为317-(2)，没有把逐列误差偷换成delta_T。

## 5. 共同效应、总响应与全局尺度对比

令C_T为(7)右侧的确定上界（隐常数取足够大的固定正值），则
E=VV*/C_T^2为正收缩。
由于RV=Q，有限维迹恒等式及317§3给
\[
 \operatorname{tr}(R\mathsf A R)_-
 \ge-\operatorname{tr}(E R\mathsf A R)
 ={ -\sum_j\langle\mathsf A u_j,u_j\rangle\over C_T^2}
 \ge {a_s-\rho_T\over C_T^2}\sum_jW_j.                     \tag{8}
\]
全部P保留在R和各方向正泄漏中；N中未用于下界的负项只合法舍去。
rho_T是317§3的统一误差。对每个j，逐方向应用314的远深正背景为
P_far,j=P_F+sum_{l!=j}P_Cl，包含其他全部选中簇，并满足相对xj的距离筛选；
它不是只含未选中深点的共同P_F。每个Wj的下界分别保证该误差统一，
因此质量不平衡不会引入Wmax/Wmin乘数。
于是(8)证明(2)第一式，
可用C{L/D+L^-3/2+sqrt(tau_T)+rho_T}控制相对系数损失。
M增长不增加该误差，因为rho_T对每个j相对其Wj统一。

取达到Wmax的簇，以该簇目标g方向应用316-(8)，有
||P||>=b_s Wmax；且每簇目标给Wmax>=c_{d0}T^{d0}/L。因此
\[
 {\lambda_T\over\|P\|}
 \le C\{L^5T^{k-d0}+\sqrt{\tau_T}\}\longrightarrow0.        \tag{9}
\]
所以常规全局逆范数乘数(1+||P||/lambda_T)^2发散，
而整个选中测试合成算子的共同代价(7)趋1。
这既不是各簇各取Rj，也不是把lambda放大到整个P范数。

## 6. 非平凡增长范围与净收益

取s=7/20、d0=2/5、theta=1/5，则Phi=8/35、k=51/140，d0-k=1/28。
例如指定r=1/(L log L)，c=1/(2 log L)，
tau=1/(2 log L)+L/T^(1/5)->0；上述所有界对允许的增长M统一。

每个选中目标对应一个实际右侧零点beta>=1/2+d0，
所以外部零密度另给M<=C L^3T^{nu(d0)}=C L^3T^(3/11)。
这只是上界；它既不产生目标，也不保证M增长。
作为量词与成本对比，假定有满足几何的M=floor(T^(1/10))个簇，
该增长率不违反上述必要计数上界或M<=1+T/D，并且定理直接适用。
这不是实际存在性证明，也没有证明这些必要条件足以实现一个zeta配置。

若只使用318的逐列HS修补，316给出的基础预算需乘sqrt(M)，
展示的基础幂变为k+1/20=29/70>d0，超过d0达1/70；
该粗证书不能再由Wmax>=c T^d0/L保证廉价。
它不证明所有这种配置中的真实||PQ||大，也不排除其他更细估计。
本篇去掉了该簇数损失，以多付log幂换取统一共同预算；
在同一窄簇宽度r=o(1/L)下无需再假设sqrt(M)c->0。
精确参数核算见scripts/collective_gram_audit.py。

## 7. 晋级与下一缺口

已通过独立内部审查的实质内容为319的实际共同远尾与本篇(3)–(9)的完整共同日程；
Schur、核展开、效应变分本身都是经典工具，317–318不单独构成新成果。
完整审查及三项澄清见[证明报告](../reviews/2026-09-06/317-320-collective-proof-review.md)；
所核读原始文献与内部287／314未陈述同一集体组合，见[来源报告](../reviews/2026-09-06/phase3-primary-literature-review.md)。
有限比较不证明世界优先权。
实际簇存在／分离及这些簇的Wtotal占总体多少仍未证明；
没有把负迹下界直接转成简单零点比例。
下一有限问题应削减外部分离或量化实际可选择簇质量，而非重复增加同级软算子。
