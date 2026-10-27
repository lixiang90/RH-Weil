# 明确修补K_g的零模／原费：独立fresh逆审

2026-10-27；/root/kg_fresh独占稿。恢复Goal／STATE／D20261027P及唯一K_g实际准入，独立复算下面的Gaussian、Poisson和费用责任。**最终有限PASS：两份实际终稿已完整核读并按本稿末尾版本绑定；修补scalar核的全部零模、空间原费及553闭包／连续mixed链闭合。** 原literal R/K及作者7.4/modularity/height的未重闭运输继续冻结；当前采用明确不同R_g版本，不改STATE/cadence/Git，不预C048/585或下一candidate。

## 1. 实际系数与B-selfdual Fourier，不偷换φ0

令B签名(1,2)，正／负投影的正平方分别P_z=B(x_+,x_+)、N_z=−B(x_−,x_−)=R_g，故2Q=P_z−N_z。实际Schwartz coefficient是

\[
 \varphi_z(x)=\varphi_g^0(x,z)e^{-2\pi Q(x)}
             =[4\pi P_z(x)-1]e^{-\pi(P_z(x)+N_z(x))}.
\]

在B-orthonormal坐标u=(u0,u1,u2)中，B=diag(1,−1,−1)，B-selfdual Haar测度是du，系数恰(4πu0²−1)e^(−π|u|²)。这里用的是φ=φ0e^(−2πQ)，没有把φ0自身当普通Gaussian。定义Fourier_B f(y)=∫f(x)e^(−2πiB(x,y))dx_B。

由普通一维Gaussian变换及其二阶导数，Fourier(u0²e^(−π|u|²))=(1/(2π)−y0²)e^(−π|y|²)。B在负坐标只反转频率，偶Gaussian／多项式不变，因而

\[
 \widehat{\varphi_z}^{,B}=-\varphi_z,
 \qquad\varphi_z(0)=-1,\qquad\int\varphi_z\,dx_B=1.
\]

每个z的B-isometry绝对行列式1，保持selfdual测度；上式对任意z成立，不需modular变换或作者theta定理。z=i的原(a,u,d)坐标给同一核(8πd²−1)e^(−2π(a²+u²+d²))，dx_B=2√2 da du dd，与上述缩放完全一致。

## 2. 精确dual/covol及两个零模

实际L=O_B∩V为fullrank3格。令c_L为dx_B的格基本域体积，L#={y:B(L,y)⊂Z}；不能把c_L混同空间vol_μ(M)。对τ=iv，K_L(v,z)=Σ_(x∈L)φ_z(√v x)。Schwartz Poisson及实际Fourier给

\[
 K_L(v,z)=-c_L^{-1}v^{-3/2}K_{L^\#}(v^{-1},z).
\]

所以large-v零项恰−1；small-v dual零项恰+c_L^−1v^−3/2。两者对z都是全局常数，因此本次P0确实杀掉两端各自的完整主项，空间导数也不产生遗漏的z-dependent leading term。这个结论来自实际多项式系数的Fourier计算，不是由字面x0或“去均值”名称猜测。

## 3. 空间导数与原norm的条件闭合链

在固定compact orbifold的有限坐标图紧提升上，正定majorant矩阵及全部固定阶z导数有uniform界。对格点和求任意固定阶空间／log-v导数，所得是有限阶多项式乘同一正定Gaussian；L及L#有固定正最短向量长度。将多项式吸收进略减的Gaussian指数，large-v非零格点尾为C_(j,k)e^(−c_(j,k)v)，small-v由上式得v^−3/2乘e^(−c/v)型尾，仍能吸收成指数界。有限charts使这些界真正是整个fixed M的C^k/H^m界，不能从一个非紧fundamental domain的坐标界直接升级。

令W(t)=e^(3t/4)P0K_L(e^t,·)，则每个fixed j,m,N的sup_t e^(N|t|)||D_t^jW(t)||_Hm有限，特别W∈L²(dt;H^m)对每个m成立。两稿已把上述actual图／格点交换完整付款，因此

\[
 \Phi_r=\int r(t)W(t)dt,
 \quad\|\Phi_r\|_{H^m}\le C_m\|r\|_{du},
 \quad C_m^2=\int\|W(t)\|_{H^m}^2dt<\infty.
\]

这是Hilbert–Schmidt充分upper，不是sharp／necessary费，不是自然height norm；原zero-extension Dlog费用再除√log2，强p_(N,0)费用由||r||du≤N^−1/2p_(N,0)(r)得到。常数依fixed model／m，没有跨B/level uniform声明。对每个m同时兼容的Bochner积分给实际C∞结果与时间／空间交换，不裁剪noncompact Pan。

## 4. Γ、F∞、component base与无限Pan的严格范围

Γ通过conjugation保L/B/Q和R，实际正常收敛的和下降到Γ\D。R_g(x,barz)=R_g(x,z)，ray τ=iv时W为实标量且conj-invariant；实r先给实F∞-invariant函数，再作复线性复化，不能把对r的复线性改成反线性。本轮fresh另实际目视既存作者PDF5：Γ\D及period λ_z(b)=b(z,1)^T给overline(λ_z(O_B))=λ_barz(O_B)，真实conjugate torus就是A_barz，故并非任意指定F∞。

全局mean-zero一般不等于逐component mean-zero；Dirichlet的closed base先明确为各组件locally constant函数。当前Γ\D却有额外实际对称性：D±各connected，Γ若交换二者则quotient连通；否则两组件由conj交换。conj保持positive体积测度，当前K在两边同值，两个组件体积／K积分相等，所以均值相同。两稿已付款这个步骤，故本actual P0K也逐组件mean-zero。此为fixed source特例，不能推广成一般globalmean事实；有向形式c*μ=−μ与positive测度保持也已区分。H¹/B_lc始终是明确合法的分离energy域。

沿553，全部实际physical Pan平移的复span在global L²du稠密。对于上述已付款的T:r↦Φ_r，它只先给

\[
 \overline{T(P)}^{H^m}=\overline{T(F)}^{H^m},
\]

不自动给exact T(P)=T(F)。由于每个m都有同原L²bound，Pan组合逼近还同时给C∞拓扑收敛；这仍是closure结论。若同一个mixed配对对实际H^m第一腿连续，且h(Tp,Tr)=0对全部P,F，则取同一Pan逼近得h(Ts,Tr)=0对全部F。无需image闭，也无需literal Tp=0或kerT=P。对H¹连续的Dirichlet配对可如此消费；自然算术height只有在实际a(Φ)类型及cited负系数/half分别确认后才可运输。

当前fixed smoothing构造即使合法，也不能据此给非零且全Pan兼容的连续完整Weil Gram；若要求exact经典身份，整pullback零与537已付正非根相冲突。不需先证明T本身非零。此逻辑不排cofinal变域、强费无du延拓、额外非局部source或未逐层消Pan的正D′。

## 5. 净等级与最终终稿绑定

上述实际费用链是标准polynomialGaussian／Poisson／compact图及553强旧的直接合成。它能判断这个明确修补源的准入，却没有新的经典primitive/RR、完整Γ/contact/properpowers/双pole、signedgrowth/actualq/core/coupling/Ξ或whole后果。支持按标准来源0轮结算并停止本fixed metric smoothing recipe，不以“无限维”或费用终于可写而虚增数学轮，也不以0轮隐藏这里已真实支付的smooth source和全部原范数范围。

已完整核读Poisson稿的selfdual measure／negative Fourier eigenvalue／covol／dual／finitecompact lifts／allspace-logv双端尾，以及费用稿的全L²→eachH^m/C∞、F∞真实period、actual组件均值、H¹/Blc／cited−E/4、无限闭包和mixed continuity。未发现实质修订项；当前结论不是仅对照相同标签。没有借P0与任意空间D交换，也没有用infinite image闭性、literalTp=0、kerT=P或T非零性。

最终绑定为UTF-8、LF规范化SHA256：

* polynomial-gaussian-poisson-and-zero-modes.md：2798004a0e9131ad76b1c4eff8b395ea05936a12719495f48993de54109dc411（9884 bytes）。
* original-fees-infinite-pan-and-net.md：93e85d624771edf7077f37890fa14feb899a750d23ec19c4aa5166ecc1f75687（10759 bytes）。

只有以上版本获本次有限PASS。任何R/Q／φ／Fourier测度／covol／空间拓扑／原费或pairing语义改动须重闭相应前件。原literal及7.4/整体theta身份仍冻结；Goal强度与最强旧wholeleading4/5负惯性UPPER保持，出稿不代root消费。root提出的下一rawmean比较只作独立准入讨论，未在本稿执行或取得新结论。
