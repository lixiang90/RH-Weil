# 原多点谱包络、完整核证书与实际零点计数

2026-10-08。作者：compression。基线 main
5b4c99e561ddec59f1818b8471da508036503745。
本稿只新增研究文本、固定来源副本和新执行输出；旧源、旧证书及原数学论文未改。

完整重放原ainta七点全域证书，并将已公开的Schwarz谱包络用于原实际零点算子，
得到可纳入项目的简单临界线比例
\[
 p_{280}=0.673009652279136912\ldots .
 \tag{1}
\]
它高于ainta原七点值；不是世界纪录，不主张新谱机制优先权。
来源与原解析输入为[R]，以下有限推导为[T]，全域执行是计算机辅助证书；
执行不代替外部解析定理或同行评审。本稿不使用原7/8条带或5/7四矩增长界。

## 1. 同一计数口径与固定来源

令 \(N(I)\) 计非平凡零点重数，\(S(I)\) 计简单临界线零点，
\(D(I)\) 计不同零点。先取 \(I=[T,2T)\)，第7节另给前缀。
置
\[
 C_0=\frac32-\frac1{\sqrt2}\cot(1/\sqrt2),\quad R_0=2-C_0,
 \quad f_0(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
                  1_{[-1/2,1/2]}(u),
\]
\[
 k_0(x)=\int f_0(u)e^{-2\pi ixu}\,du,\qquad w(x)=k_0(x)^2 .
 \tag{2}
\]
与验证器的
\((\sinc(\pi x-\beta)+\sinc(\pi x+\beta))/(2\sinc\beta)\) 相同，
\(\beta=1/\sqrt2\)；未漏除 \(K(0)=\sqrt2\sin\beta\)。

实际AF输入取归档
[v2原论文](../../literature/baseline/2026-alpoge-furman-6725-v2.pdf)，
已核读§2.2–2.3、Lemma2.1、Propositions4.1–4.3、Theorem5.7和§6。
raw SHA256为
6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444。
直接Hilbert第二接口取
[304 §5](../../notes/304-mt-triple-geometry-and-second-moment-stability.md)，
canonical LF SHA256
03f21ab1749157ff45bc4d4f62709e2a5482257c7155e7e8e644da0ac4521bc4。

ainta [固定提交040c5e8](https://github.com/ainta/zeta-simple-zeros/tree/040c5e899e658aed7b56a2a87f501798fe10761d)
的 [原PDF](../../literature/candidates/2026-ainta-6730085-040c5e8.pdf)
全7页已读，raw SHA256
d846f3a73cf3ab012d7c16be78c5bab35fcd5d2b1d99db5bf036bd638a277afc。
七个Python模块执行前逐行核读，副本和原MIT许可见
[来源清单](artifacts/hybrid-multipoint-ainta-040c5e8/source-manifest.json)。
它们只用于有限核证书，没有网络执行器或新增解析输入。

完整谱包络归
[Schwarz固定提交e2453c1](https://github.com/uwe-schwarz/zeta-simple-zeros-673026/tree/e2453c1cafc1387ef553fe6bee74d1f5223ba801)。
本轮独立读paper/riemann.tex原383–501行及完整docs/proof.md；
精确来源与根线程独立证明见
[source-read](hybrid-multipoint-spectral-envelope-source-read-root.md)，
canonical LF SHA256
2c4a81a9a2d860e3d0882edb8a1a5928cda318679874c9be9b0adf18576b5dc5。
未重放该来源较强的382623/10^8局部证书，也不导入其67.302666%主张。

## 2. 范数至多1列的实际惯性余项 [T]

定义非负凸函数
\[
 j(t)=
 \begin{cases}(t-1)^2,&0\le t\le2,\\2t-3,&t\ge2.\end{cases}
 \tag{3}
\]
它在 \([0,\infty)\) 上为2-Lipschitz；只用标量凸性。
设 \(V\) 有 \(s\) 列，每列范数至多1，
\(P=VV^*\)、\(G=V^*V\)、\(A=P+Q\)、\(n_+(Q)\le b\)。则
\[
 4\operatorname{tr}A-\|A\|_{\rm HS}^2
 \le4b+2\operatorname{tr}P+s-\operatorname{tr}j(G)
 \le4b+3s-\operatorname{tr}j(G).
 \tag{4}
\]
给环境补零至维数至少 \(s+b\)，令 \(p_i\) 为 \(G\) 的全部谱。
最小最大原理给 \(\lambda_{b+i}(A)\le p_i\)：
正交掉 \(Q_+\) 的像与 \(P\) 前 \(i-1\) 个谱向量即可。
对前 \(b\) 个谱用 \(4t-t^2\le4\)，后续用
\[
 t\le p\ \Longrightarrow\
 4t-t^2\le\phi(p):=
 \begin{cases}4p-p^2,&0\le p\le2,\\4,&p\ge2,\end{cases}
 \qquad \phi(p)=2p+1-j(p).
\]
剩余 \(p=0\) 的空间谱有 \(t\le0\)，贡献至多0。
求和即得第一式，\(\operatorname{tr}P\le s\) 给第二式。
Gram零特征值计在这 \(s\) 个谱内；环境补零不额外计 \(j(0)\)。

若实际账本另给 \(s+2b\le N_c\)、\(D_c\ge s+b\)，则
\[
 s\ge4\operatorname{tr}A-\|A\|_{\rm HS}^2-2N_c+J,\qquad
 D_c\ge\frac{4\operatorname{tr}A-\|A\|_{\rm HS}^2-N_c+J}{2},
 \quad J=\operatorname{tr}j(G).
 \tag{5}
\]
第二式由 \(4b+3s\le N_c+2D_c\) 得出；
没有使用一般不成立的 \(D_c\ge(N_c+s)/2\)。

## 3. 原AF实际列、尾项与紧跨度核 [T/R]

沿用原 \(L=\log(T/(2\pi))\)、\(h=2\pi/L\)、
\(\alpha_k=T+kh\)、\(d=\lfloor LT/(2\pi)\rfloor\)，
\[
 \phi(u)=\chi(L/2+u)\chi(L/2-u)\sqrt{\cos(\sqrt2u/L)},
 \qquad a_L=\|\phi\|_2^2/L .
\]
上式在 \(|u|\le L/2\) 内取值，区间外定义为0；
置 \(\gamma_\rho=(\rho-1/2)/i\)，其实部是普通零点高度。
固定原taper \(\chi\)，简单临界线零点的列为
\(v_\rho/\sqrt{a_LL^2}\)，
\(v_\rho=(\widehat\phi(\gamma_\rho-\alpha_k))_{0\le k<d}\)。
原全Gabor Poisson恒等式给列范数至多1，精确满足(4)；
不是把对角近似1直接当成单位列。

令 \(I'=[T-\sqrt T,2T+\sqrt T)\)，
\(A=\widetilde G\) 为 \(I'\) 的真实零点有限算子；
实际prime-side矩阵是 \(\widetilde G+\widetilde E\)。
精确地 \(A=(a_LL^2)^{-1}\sum_{\Re\gamma_\rho\in I'}m_\rho v_\rho v_\rho^T\)；
离线对的列为 \(v,\bar v\)，写 \(v=a+ib\) 后其块是
\(2m_\rho(aa^T-bb^T)/(a_LL^2)\)，故整个 \(A\) 实自伴。
原合同为
\[
 \|\widetilde E\|_1=O_\chi(T^{-1/2}),\quad
 \operatorname{tr}A=N(I')+o(N(I)),\quad
 \|A\|_{\rm HS}^2=(R_0+o(1))N(I).
 \tag{6}
\]
这是未归一化Schatten1合同。平方范数传递误差至多
\(2\|\widetilde G+\widetilde E\|_{\rm HS}\|\widetilde E\|_{\rm HS}
 +\|\widetilde E\|_{\rm HS}^2=o(N)\)。
不把normalized \(o(N)\) 错用作这里的 \(o(1)\)。

设 \(s_1,s_2,p\) 是 \(I'\) 中简单临界线点、重复临界线点、不同离线对数。
取 \(P\) 为全部简单列和、\(Q=A-P\)。原pull-back给
\[
 n_+(Q)\le b=s_2+p,\quad s_1+2b\le N(I'),\quad
 D(I')=s_1+s_2+2p\ge s_1+b .
 \tag{7}
\]
离线块保留正负signature，未假设全Weil正性。
\(I'\setminus I\) 重数计数为 \(O(\sqrt T\log T)=o(N(I))\)。
将(5)用于同一实际算子得
\[
 S(I)\ge C_0N(I)+J^\circ-o(N(I)),\quad
 D(I)\ge\frac{(1+C_0)N(I)+J^\circ}{2}-o(N(I)).
 \tag{8}
\]
\(G^\circ\) 是保留中心简单零点的主Gram块，
\(J^\circ=\operatorname{tr}j(G^\circ)\)。
从全Gram pinching并丢其余非负 \(j\) 块得 \(J\ge J^\circ\)。

保留位置 \(x=(\gamma-T)/h\) 距grid两端至少 \(L^2\)。
删除的普通高度区间长 \(O(L)\)，由短区间零点计数只删除 \(O(L^2)=o(N)\) 点。
任意固定跨度 \(R\) 内，原全grid恒等式与实轴 \(r^{-2}\) 尾给
\[
 (G^\circ)_{ij}=
 \frac{\widehat{\phi^2}(h(x_i-x_j))}{a_LL}+o(1)
 =k_0(x_i-x_j)+o(1)
 \tag{9}
\]
一致成立。末步用 \(\phi(Lu)^2\to\cos(\sqrt2u)\) 的 \(L^1\) 收敛，
只在实轴紧集逼近。
端外平方列尾除 \(a_LL^2\) 后为
\(O_\chi((LD^3)^{-1})=O_\chi(L^{-4})\)，普通端距 \(D\gg L\)；
所以保留对角一致为 \(1-o(1)>0\)。
跨度与列数均不随 \(T\) 增长。

## 4. 完整七点与独立有理三点证书 [T，计算机辅助]

对六个非负gap，原目标为
\[
 F_6(g)=\frac1{3000}\sum_{i=1}^6g_i+
 \sum_{r=1}^6\frac2{7-r}\sum_{i=1}^{7-r}
   w(g_i+\cdots+g_{i+r-1})\ge\tau=\frac{19}{5000}.
 \tag{10}
\]
局部pressure是1/3000，不是1/500。
新 [runner](../../scripts/hybrid_multipoint_cap_replay.py)
导入前检查7模块原rawhash与原MIT许可，禁止覆盖任何已有输出，
无网络调用、bytecode或旧源写入。canonical LF SHA256：
8ac87f18cf928a51771556168e5af07400a3ba0333196b3e410394d8e4c37d05。

从根目录运行python -B -X utf8 scripts/hybrid_multipoint_cap_replay.py seven。
[新输出](../../output/hybrid-multipoint-seven-primary-replay.json)
canonical LF SHA256
aa6885489c1d0086bca32b72d27fc7a2a5f44a48f78483a057f23a59e5a828e6。
全栈耗尽后才生成verified=true；实际耗时73.5774499秒：

- 707901 nodes、354315 pruned、353586 splits、depth37、729 initial boxes；
- pressure3087、interval257493、convex tangent93735，三者和354315；
- 存活gap closed cells：[3809,4778]、[7221,9363]、[10572,44827]；
- \(w\) 表SHA a9992300d2bf71665aa2b6bd2727e798624cd297103bb200c7f0ca2baea55a2c；
- \(w''\) 表SHA 7913c5511a572c32dd573cd53123d8cf3ddf73d3ec63b1aa823faae2ae83570a。

域外 \(\sum g_i\ge11.4\) 由pressure支付。
整数剪枝精确 \(45600/(4000\cdot3000)=19/5000\)，未依float相等。
Arb闭cell下界再向下舍入、目标向上舍入；
多gap频率cell inclusive范围是
\([\sum{\rm low},\sum{\rm high}+r-1]\)，不漏边界。
超表长 \(w\) 下界取0，二导数下界取负无穷。
负二导数下界用向上系数，正下界用向下系数，其外积和为真实Hessian的Loewner下界。
float LDL仅筛选，随后精确binary64有理数重建Arb矩阵并认证正pivot，
才可使用凸tangent。终端cell未解抛错，无节点截断或部分PASS。

附独立加强304的小型有理核证书：
\[
 w(a)+w(b)+w(a+b)\ge221/10^6
 \quad(a,b\ge0,\ a+b\le4).
 \tag{11}
\]
用冻结项目RationalKernel的Machin、整数平方根、48阶sinc与Lipschitz包络，
完整覆盖445581 boxes、333733验收叶、453域外叶、depth19；
\(445581=111395+333733+453=1+4\cdot111395\)。
4172缓存中心，耗时1.4899439秒。
[新输出](../../output/hybrid-multipoint-three-rational-replay.json)
canonical LF SHA256
4ee77471d08503c22a848e47a17713b44bd5f2afb95bfd57d994e878d9192456。
所有验收均精确整数比较，float不决定成功。
这认证已公开阈值，不是新发现三点机制；(1)只用(10)，不叠加同Gram两份余项。

## 5. 已知完整谱包络与固定280点实际主块 [T/R]

对单位对角 \(m\times m\) correlation matrix \(R\)，
\(E=\operatorname{tr}(R-I)^2=2\sum_{i<j}|R_{ij}|^2\)，
Schwarz包络为
\[
 \operatorname{tr}j(R)\ge g_m(E)=
 \begin{cases}
 E,&0\le E\le m/(m-1),\\
 E/m+2\sqrt{(m-1)E/m}-1,&m/(m-1)\le E\le m(m-1).
 \end{cases}
 \tag{12}
\]
独立核对：谱写 \(1+y_i\)、\(\sum y_i=0\)。
全部 \(y_i\le1\) 时 \(J=E\)。否则在 \(h\) 个 \(y_i>1\) 上写
\(y_i=1+u_i\)，\(r^2=\sum u_i^2\)、\(\sum u_i\ge r\)；
其余偏差和为 \(-h-\sum u_i\)。Cauchy给
\[
 E\ge h+2r+r^2+\frac{(h+r)^2}{m-h}
 =\frac{m(1+r)^2}{m-1}
  +\frac{(h-1)(m+r)^2}{(m-h)(m-1)}.
 \tag{13}
\]
\(E-J=r^2\) 给(12)。第二分支只能在 \(E>m/(m-1)\) 发生；
两分支连续、递增、1-Lipschitz。
故 \(E+x\ge A,x\ge0\) 蕴含 \(g_m(E)+x\ge g_m(A)\)。

将(10)在 \(m-6\) 个连续七点窗口上求和，
每gap至多计6次，跨度 \(r\le6\) 的pair至多计 \(7-r\) 次；
所有系数非负，得
\[
 E_m+\frac{{\rm span}}{500}\ge A_m=\tau(m-6),
 \qquad E_m=2\sum_{i<j}w(x_i-x_j).
 \tag{14}
\]
明确固定 \(m=280\)，
\[
 A=2603/2500,\qquad
 C=g_{280}(A)=\frac{2603}{700000}
                 +2\sqrt{\frac{726237}{700000}}-1 .
 \tag{15}
\]
无需也不主张280为所有整数块长的全局最优。

实际有限 \(G_B\) 只是范数至多1列的Gram。
小跨度分支令
\(D_B=\operatorname{diag}((G_B)_{ii}^{-1/2})\)、\(R_B=D_BG_BD_B\)，
后者精确单位对角。
由(9)保留对角一致 \(1-o(1)\)，Gram Cauchy给 \(|(G_B)_{ij}|\le1\)，
固定280点下 \(\|R_B-G_B\|_{\rm HS}=o(1)\) 一致。
Hoffman–Wielandt与(3)在非负谱上的2-Lipschitz给
\[
 |\operatorname{tr}j(R_B)-\operatorname{tr}j(G_B)|
       \le2\sqrt m\,\|R_B-G_B\|_{\rm HS}=o(1),
 \qquad E(R_B)=E_m+o(1).
 \tag{16}
\]
故每个280点实际主块满足
\[
 \operatorname{tr}j(G_B)+\frac{{\rm span}(B)}{500}\ge C-o(1).
 \tag{17}
\]
若 \({\rm span}/500\ge A\)，由 \(j\ge0,C\le A\) 直接成立。
否则 \({\rm span}<500A=520.6\)，用(9)的固定 \(R=521\)。
归一化、核近似与(12)–(14)只损失一致 \(o(1)\)；
用 \(g(A-\varepsilon)\ge C-\varepsilon\)，先取 \(T\) 大使 \(A-\varepsilon>0\)。
没有无误差升级到单位对角，亦未误留旧500跨度阈值。

## 6. 全部平移分块与实际比例闭合 [T/R]

保留简单点数 \(S^\circ=S(I)-o(N(I))\)，位置区间长
\(d+O(1)=N(I)+o(N(I))\)。
对280种offset分成满280点连续主块，两端至多 \(2(m-1)\) 点。
对每种分块，标量Jensen在各块本征基给
\[
 J^\circ\ge\sum_B\operatorname{tr}j(G_B).
 \tag{18}
\]
未用operator convexity；剩余PSD块的 \(j\) 迹非负。
满块平均数 \(S^\circ/m+O(1)\)。
每相邻gap在280种offset至多属于279个block spans。
由(17)平均
\[
 J^\circ\ge \frac C{280}S(I)
       -\frac{279}{500\cdot280}N(I)-o(N(I)).
 \tag{19}
\]
块误差一致 \(o(1)\)，块数 \(O(N)\)，总误差 \(o(N)\)；
参数 \(m,R,\chi\) 均先固定。
代入(8)，\(280-C>0\)，得
\[
 \liminf_{T\to\infty}\frac{S(T,2T)}{N(T,2T)}
 \ge p_{280}:=\frac{280C_0-279/500}{280-C}.
 \tag{20}
\]
不同点用(8)第二式、同一(19)和(20)：
\[
 \liminf_T\frac{D(T,2T)}{N(T,2T)}
 \ge\frac{1+C_0-279/(500\cdot280)+(C/280)p_{280}}2
 =\frac{1+p_{280}}2.
 \tag{21}
\]
等号来自 \((1-C/280)p_{280}=C_0-279/(500\cdot280)\)，
非任意配置的 \(D\ge(N+S)/2\)。

新 [精确代数输出](../../output/hybrid-multipoint-cap-exact-algebra.json)
canonical LF SHA256
d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3
用128bit有理Machin、cos/sinc Taylor和整数平方根给严格区间，得
\[
 p_{280}>\frac{673009652279}{10^{12}}>p_{270}>p_{269},\quad
 p_{269}=\frac{1345000C_0-2680}{1340003}
        =0.673008527927779761\ldots .
 \tag{22}
\]
初始范数列cap \(m/(m-1)\) 可得270点
\(p_{270}=0.673008712346916931\ldots\)，但已被(12)覆盖，
不另算可加增益。
(20)显示67.3009652279…%，不同点显示83.6504826139…%。
七点与有理三点均已分别第二次完整--check通过；
比较确定字段全部相同，未覆盖首次执行的runtime或输出。

## 7. 304直接单位列第二桥与极限次序 [T/R]

此桥给前缀 \(0<\gamma\le T\) 的同一实际比例，不使用Gabor对角近似。
按304§5取固定实偶
\(\eta_\delta\in C_c^\infty((-1/2,1/2))\)、\(\int\eta_\delta^2=1\)，
\(f_\delta=\eta_\delta^2\to f_0\) 于 \(L^1\cap L^2\)，
\(k_\delta=\widehat f_\delta\)。
设 \(\varepsilon_\delta=\|f_\delta-f_0\|_1\)，
\(\sup_{\mathbb R}|k_\delta-k_0|\le\varepsilon_\delta\)，两实核模至多1。

304已付去权合同对每个固定 \(\delta\) 给实际全复零点算子
\[
 \operatorname{tr}A_{\delta,T}=N(T),\quad
 \|A_{\delta,T}\|_{\rm HS}^2=(R_\delta+o_\delta(1))N(T),
 \qquad R_\delta\to R_0 .
 \tag{23}
\]
具体去权仍用 \(Q_\delta=f_\delta*f_\delta\) 及其二导数，
将相关权与 \(k_\delta(z)^2\) 的精确恒等式分成两份固定测试函数；
未将随 \(T\) 变函数插入固定函数定理。
离线特征保留 \(g_z,h_z\) 的正负rank1块；
共轭重排只在全部复零点双和进行，未删除非正项。
简单实点列 \(v_x=\eta_\delta e^{-2\pi ixu}\) 精确单位，
Gram条目精确 \(k_\delta(x_i-x_j)\)。
位置长度 \(X_T=TL/(2\pi)\) 满足 \(X_T/N(T)\to1\)；
实际仍有 \(N(T)\ge s+2b,D(T)\ge s+b\)，(5)适用。

固定 \(m=280\) 时实核能量改变量至多
\[
 e_\delta=2m(m-1)\varepsilon_\delta .
 \tag{24}
\]
这是 \(2\sum_{i<j}\) 乘每平方差至多 \(2\varepsilon_\delta\)。
由(14)，每实际块 \(E_\delta+{\rm span}/500\ge A-e_\delta\)。
先固定小 \(\delta\)，使 \(A-e_\delta>0,C-e_\delta>0\)；
包络单调性与1-Lipschitz给
\[
 \operatorname{tr}j(G_{\delta,B})+{\rm span}/500\ge C-e_\delta.
 \tag{25}
\]
实轴误差全域一致，此桥不用另设跨度cutoff。
平移分块按(18)–(19)，将 \(C\) 换为 \(C_\delta=C-e_\delta\)、
位置长度换为 \(X_T\)。
先 \(T\to\infty\)，得
\[
 \liminf_T S(T)/N(T)\ge
 p_\delta=\frac{2-R_\delta-279/(500\cdot280)}{1-C_\delta/280},
 \qquad\liminf_T D(T)/N(T)\ge(1+p_\delta)/2 .
 \tag{26}
\]
最后 \(\delta\to0\)，\(p_\delta\to p_{280}\)。
先固定profile、再高度、再profile极限，没有 \(\delta(T)\) 统一误差假设。
可独立作为前缀接口；亦可从dyadic(20)求和，
固定足够大起点，有限低高度贡献除 \(N(T)\) 消失。
不同点账本均保留。

## 8. 结果范围与复跑

本轮把已知七点核与已知谱包络完整审读、真实全域执行，
恢复原对象的迹、尾、惯性、单位列误差和分块合同，
使项目可采纳比例严格超过304值及ainta原七点值。
这是具体有限证书加原已知算术合同，不是新增小Q或四矩假设。

[305文献审计](../../notes/305-post-6725-literature-baseline-audit.md)中
67.3316977%与67.3399%后续公开主张均更高，
其本项目尚未完成认证不被本轮较弱结果取代。
Schwarz、ainta、Shi有先行来源；
不称世界首次或最新纪录。比例是渐近零点计数下界，
不是RH证明完成百分比。full signed近共振和常数级四矩预算仍未由(20)支付。

新runner提供algebra、seven、rational-three模式。
加--check会完整重放，除runtime外比较全部确定字段，且不写文件。
失败限额报错退出；旧源与旧JSON未覆盖。
脚本明确不认证analytic transfer或world record。
本稿另给数学传递证明，仍需独立作者全文审查后冻结。
