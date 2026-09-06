# 317. 分离深目标的共同Gram与原算子的集体测试效应

2026-09-06，phase 3第1轮。[T，待独立复核]；实际簇条件仍[C/O]。
本轮是经典核界／Schur／效应机制的自含重建，不单独计为阶段新算术成果。

## 1. 对象和量词

沿用316：同一实际前缀0<gamma<=T、L=log T、A=L/2、sharp MT密度eta_A^2，
原算子mathsf A=P-N，全部原始重数与正负列保留。
固定0<s<d0<1/2与theta>0。选M>=1个互不相交深点簇Cj，
各有目标zj=xj+i dj，dj>=d0；中心相距至少D=T^theta。
各簇满足316的直径r、深度>s和对所有簇外深点的D分离条件。
M可随T增长；常数不依赖M、目标位置及单点重数。存在性不在定理中证明。

取uj=hj/sqrt(Hj)，Q=[uj]，Wj为316的簇负列总质量。
Q是测试矩阵，不是原算子负列因子。Wj不是负谱迹。

## 2. 归一化核的统一远界

313-(4)将hh、gg、gh内积展开为四个MT核，给
\[
 |\langle h_{x+ia},h_{y+ib}\rangle|
 \le C {e^{A(a+b)}\over A|x-y|},\qquad |x-y|\ge1.
\]
对a,b属于固定[s,1/2)，端点长度1积分给
Ha,Hb分别至少c_s e^{2Aa}/A、c_s e^{2Ab}/A。
故归一化后
\[
 |\langle \widehat h_{x+ia},\widehat h_{y+ib}\rangle|
 \le {C_s\over |x-y|}.                                      \tag{1}
\]
将任一h换成g同样成立：G=1+H>=H保证分母下界，分子仍有相同核估计。
常数统一到深度趋近1/2；只要求正下界s固定。
实型Hilbert空间中的内积为实数；在辅助复L2中取绝对值的界也适用。

按xj递增排序，有|xj-xk|>=D|j-k|。令ell=1+log M，M=1时ell=1。
单位对角线与(1)给每行非对角绝对值之和至多C_s ell/D。
因此自伴矩阵Schur界给
\[
 \|Q^*Q-I_M\|\le C_s\ell/D=:\epsilon_T,\qquad
 \|Q\|^2\le1+\epsilon_T.                                    \tag{2}
\]
由于xj在(0,T]，M<=1+T/D，ell<=C L，故epsilon_T=O(L/D)=o(1)。
这里无重数乘M：每簇仅选一个归一化测试方向，原始重数留在P和N中。

## 3. 一个共同效应才允许求和

有限维自伴算子B及正收缩E满足-tr(EB)<=tr(B_-)，
因为B=B_+-B_-且tr(EB_+)>=0、tr(EB_-)<=tr(B_-)。
取E=QQ*/(1+epsilon_T)，由(2)它是正收缩，故
\[
 \operatorname{tr}(\mathsf A_-)
 \ge{-\sum_{j=1}^M\langle\mathsf A u_j,u_j\rangle
        \over1+\epsilon_T}.                                \tag{3}
\]
此式不要求uj彼此正交；分母不能省略。

若另有316的固定参数k=max(s,1/4+Phi_s(theta)/2)<d0及c=Ar->0，
316-(9)连同全部浅点、临界线与远深正项的误差给
\[
 -\langle\mathsf A u_j,u_j\rangle\ge(a_s-\rho_T)W_j,
\quad
 \rho_T\le C\{c^2+L^2T^{-d0}+L^2T^{s-d0}+L^4T^{\Phi_s(\theta)-d0}\}=o(1).
\]
常数统一于j，Wj>=c_{d0}T^{d0}/L；所有其他负列只在合法下界中舍去。
故
\[
 \operatorname{tr}(\mathsf A_-)\ge
 {a_s-\rho_T\over1+\epsilon_T}\sum_jW_j.                     \tag{4}
\]
这是原算子共同效应的条件性推论，不是不同Rj所得压缩负迹的求和。

## 4. 尚需处理的共同逆变换

对同一lambda>0、R=lambda(P+lambda I)^-1，令V=R^-1 Q=Q+PQ/lambda。
效应VV*/||V||^2可用于R mathsf A R，但(2)并不控制||V||。
下一轮审计逐列小量与||PQ||的区别；不能由316逐列结论直接宣布共同压缩成立。
经典背景与原始文献的独立比较另行保存，不作世界优先权声明。
