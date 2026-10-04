# 424 独立全文复核：相对锥、连续不变扩张及四分量范围

2026-10-04。复核对象：
[424](../../notes/424-f1-relative-chain-repair-and-four-component-obstruction.md)。
本次首轮核读 SHA256：
`bbf9edc00944656c550f0b4266e967e4eb6ae1092aa27bfae8c02ab642414d40`。

最终七节采纳版本 SHA256：
`23b1ca33824e7420e5c55a8f636a0ac9654ed2ee1f21601b147ef2cb174eaf23`。
最终状态：限定 PASS；新增源节及前提补明均经下面的采纳复核。

结论：当前六节版本的核心构造及限定障碍通过独立复核；未发现 P1/P2 级公式错误。
下述定义及范围建议应补明。PASS 只覆盖指定代数链和连续读出，
没有认证完整循环 Chern 类、原源规范理想类、主关系消失或 RH。
若正文改变，必须补充采纳复核并绑定新哈希，不能以本快照代替后来版本。

## 1. 定义域、Hochschild 方向与相对锥

422 已给 \(\mathcal I\) 在 \(\mathcal M\) 左右作用下保持，故
\(\mathcal M/\mathcal I\) 的**代数商**及至少一条 \(\mathcal A/\mathcal I\) 腿的链有定义。
本稿明确只用有限代数张量，没有声称 \(\mathcal I\) 在乘子的算子拓扑中闭，
也没有偷偷引入一个完备拓扑商。
若任一腿在 \(\mathcal I\)，该腿是实际整个空间上的迹类算子，其他乘子有界，
所以 \(D=0\)；\(\kappa\) 在理想上为零，因此 \(E=0\)。
这足以使 \(E\) 下降到正文实际采用的代数商链。

边界符号准确为
\[
 b_\alpha(A\otimes B)=AB-\alpha(B)A,
\]
\[
 b_\alpha(A\otimes B\otimes C)
 =AB\otimes C-A\otimes BC+\alpha(C)A\otimes B.
\]
继续展开，\(ABC\)、\(\alpha(C)AB\)、\(\alpha(B)\alpha(C)A\) 各出现一次正号及一次负号，
所以 \(b_\alpha^2=0\)。其余公式没有将右侧系数错误地留在未平移位置。

相对锥约定
\(R_n=X_n\oplus Y_{n+1}\)、
\(\partial(x,y)=(bx,qx-by)\) 正确：
第二次边界的第二项是 \(qbx-bqx+b^2y=0\)。
度零应理解为包含 \(R_{-1}=Y_0=\mathcal A/\mathcal I\)，
于是合法相对零循环恰满足 \(qx=by\)。
在此约定下 \((bz,qz)=\partial(z,0)\) 确为循环及边界，
\(\mathcal P(bz,qz)=\varphi(bz)-\bar E(qz)=0\)。

定义建议：正文显式写出 \(R_{-1}=Y_0\) 和零循环条件 \(qx=by\)，
避免把锥截断在非负次数后误读成任意 \((x,y)\) 都是循环。
这项补明不改变现有证明或结论。

## 2. 实际源、\(D/E\) 传递及非平凡类的范围

\(A=T^*\) 是实际有界连续乘子，\(B=TK_h\in\mathcal A\)，
所以 \(z_E=A\otimes B\) 和其全部边界合法。
其完整相对值为零来自精确锥边界，并不是仅消掉混合原子。

\(z_D=A\otimes B-1\otimes B\sigma(A)\) 也有实际迹类腿，
且
\[
 b_\alpha z_D=AB-\alpha(B)A-B\sigma(A)+\alpha(B\sigma(A))
             =AB-B\sigma(A).
\]
这里 \(\alpha(B\sigma(A))=\alpha(B)A\) 保留完整群乘法。
进一步 \(E(1,B\sigma(A))=\kappa(\alpha(B)A)\)，
故 \(\bar E(qz_D)=D(A,B)\)，正文 (8) 及其相对抵消正确。

正文 (9) 也有精确自由度解释：固定 \(y=qz\) 的循环必有
\(i=x-bz\in\mathcal I\)，配对等于 \(\operatorname{Tr}(iW)\)。
所以原文正确地只停止同一两因子提升给出的 exact cone；
它没有否定任意非平凡相对 K/Chern 类，也没有把自由指定的 \(i\) 认作原源主关系。

实质未支付项仍在这里：尚无由原 \(u\)、条带、壳层及时间测试共同构造的规范
非零 \(i\)，也没有其与全部 \(A_N(h)\) 及两个独立半迹归一化的比较。
相对边界为零不能填补这项来源缺口。

## 3. 连续不变标量扩张与固定测试

实际序列恒等式
\[
 \beta_{(r,s)}(H(j)\delta_k(l))
 =H(j)\delta_{k+s}(l)+[H(j-r)-H(j)]\delta_{k+s}(l)
\]
的余项全和是 \(-r\)，不是 \(+r\)。
\(\Phi\circ\alpha=\Phi\) 后得到
\(\Phi(F_{k+s})-\Phi(F_k)=r\)，正文符号正确。
固定群标签切片的每个 \(p_n\) 值一致，连续线性泛函在这族上确实必须有界。
三种情况 \(r\ne0,s=0\)、\(r\ne0,s\ne0\)、\(r=0,s\ne0\) 完全覆盖全部非零标签。
因此无连续不变标量扩张的结论无需额外假设它是扭曲迹。

\(\mathcal A^\sigma=0\) 也正确。需要的“某坐标趋负无穷时一致消失”可由
四分量展开直接验证；例如 \(j\to-\infty\) 时 \(H(j)\) 为零，
\(r_p(j)\) 及 \(\sup_k\|r_{pq}(j,k)\|_1\) 均趋零。
这使沿平移轨道的论证即使另一坐标趋正无穷也成立。
有限格点值全零再使边、角极限全零。

Cesàro 见证的 \(p_0=\varphi=1\) 正确。
实际上对应径向正交投影平均的算子范数是 \(1/(2N+1)\)，
因而比正文的“点态、强趋零”还强；它仍不在原 Fréchet 拓扑中收敛。
这没有否定乘子 \(u\) 的固定性。

## 4. 四分量模型的 coinvariant、非分裂与最小维数

\(N_1,N_2\) 的全部符号正确，两者的非零复合均只将 \(c_0\) 送到 \(t_0\)。
因此
\(S(a,b)S(u,v)=S(a+u,b+v)\)。
\((S(1,0)-1)V=\operatorname{span}\{t_0,q_0\}\)，
\((S(0,1)-1)V=\operatorname{span}\{t_0,p_0\}\)，
故 \(V_\Gamma\cong\mathbb C[c_0]\)；全 \(\Gamma\) 不变线性泛函只能读角点。

扩张非分裂见证 \(p_0\) 模 \(t_0\) 后固定，而其任意提升被 \(S(1,0)\) 改变
\(-t_0\)，正确。相容线性商若保留 \(Q(t_0)\ne0\)，核对 \(N_1,N_2\) 保持；
依次施 \(N_1N_2,N_1,N_2\) 迫使核的四个系数均为零。
所以模型内四维下界正确，且不要求目标半单或酉。
该下界使用完整两生成元 \(\Gamma\) 作用，不能不加说明地用于只保留一个固定 \(\gamma\) 的模型。

已独立阅读正文引用的
[四分量推导](f1-four-component-relative-obstruction-derivation.md) §6。
它对更一般实际 \(E_2\) 连续有限维目标的四维下界，还要求
\[
 Q(r)=(\sum r)t_W\quad\text{对全部开放 }r\in\ell^1(\mathbb Z^2),
 \quad t_W\ne0.
\]
即开放余项仅映向固定迹轴；连续性提供有界边轨道，有限维广义特征空间投影
再提取实际四维非分裂子模。该证明本身正确。
正文的概括建议同时显式保留“开放余项仅映固定迹轴”，
不能只说连续／有界轨道便将下界推广给允许额外开放数据的任意目标。

## 5. 循环缺陷、\(G\) 层级及第二个锥

独立展开得到
\[
 E(A,B)+E(\alpha(B),A)=\varphi(AB)-\varphi(\alpha(AB))
                         =\kappa(\alpha(AB)),
\]
所以正文 (15) 的 \(\alpha\) 方向及符号正确。
\(G\) 同时对余链输入施 \(\sigma\)，\(G\) 与 \(b_\alpha\) 交换；
于是 \((G-1)E=b_\alpha\kappa\)。
实际四分量给
\[
 \kappa=r\operatorname{Tr}e_p+s\operatorname{Tr}e_q
                          +rs\operatorname{Tr}f_c,
\quad (G-1)\kappa=2rs\operatorname{Tr}f_c,
\quad (G-1)^3\varphi=0.
\]
单轴时二阶项为零，但一阶异常及扩张障碍仍存在。

正文关于不变性锥的叙述，可用明确度数补明：
\(K^n=C^n\oplus C^{n-1}\)，
\[
 d(x,y)=(b_\alpha x,(G-1)x-b_\alpha y).
\]
由交换关系 \(d^2=0\)，且 \((E,\kappa)=d(\varphi,0)\)，
\(d(E,\kappa)=0\)。因此它在全域上确为 exact。
这仍没有消去 (15) 的标准循环缺陷，不能认作完整扭曲循环 Chern 配对。

已核查 [Ponge 原文页面](https://arxiv.org/abs/1810.04835)：
作者、标题及 para-S 背景对应准确，原文也区分 paracyclic 数据和真正链复形。
正文没有调用该文来替代实际循环准入证明，其引用范围适当。

## 6. 建议合并的实际源链障碍

下面是 [独立链推导](f1-relative-chain-derivation.md) 的新输入，
首轮六节版本未包含，最终七节版本已采纳并重新核验。
角点 \(\alpha=\mathrm{id}\) 上
\[
 b(u^*\otimes uk)=k-uku^*.
\]
可用允许的原测试给严格非零见证：\(d=c(t)\varphi([t])\)，
圆周支集与其 \(M\) 旋转支集不交；取 \(h\) 在
\(\operatorname{supp}d-\operatorname{supp}d\) 上恒 1，则
\(k=|d\rangle\langle d|\)，而 \(ud=c(t)\varphi([t-M])\) 与 \(d\) 正交。
所以单次插入 \(k\) 不是角点源的 Hochschild 循环。

自然对称修复满足
\[
 z_{\rm sym}=u^*\otimes uk-ku^*\otimes u
            =1\otimes k-b(u^*\otimes u\otimes k).
\]
它虽闭，但角点 Hochschild 类与 \(u\) 无关。
提升公式应完整保留右侧 \(\alpha(K)\)：
\[
 T^*\otimes TK-\alpha(K)T^*\otimes T
 =(T^*T)\otimes K-b_\alpha(T^*\otimes T\otimes K).
\]
最终正文准确限定为该特定对称链的 Hochschild 类退化，
没有扩大为所有高次循环 Chern 类或相对理论不存在。

## 7. 核验结算

当前版本的数学结论限定 PASS。尚未支付的实质问题是完整循环链准入和原源规范理想类／周期比较；
正文对此保持开放，故不是当前有限命题的错误。
建议补明锥的负一次项、第二锥的度数，以及一般四维下界的开放迹轴前提。
若主稿采纳源链新节或改变内容，需要记录采纳复核及最终哈希。

## 8. 最终采纳复核

对最终七节正文重新读取并独立计算 SHA256，确认为
`23b1ca33824e7420e5c55a8f636a0ac9654ed2ee1f21601b147ef2cb174eaf23`。

1. 已明确 \(R_{-1}=C_0(q)\)、零循环 \(qx=by\)；度数及边界符号准确。
2. 已加入不变性余链锥微分，\(d\varphi=(E,\kappa)\) 与 \(d(E,\kappa)=0\) 符号准确。
3. 一般 min4 概括现在要求 \(Q(r)=(\sum r)t_W\)，并单独写 \(t_W\ne0\)。
   它不再错误要求每个迹零余项像非零；完整平移相容、连续及有限维前提仍引用独立报告。
4. 新增秩一见证已明确角点字符 \(\zeta=(1,1)\) 的实际时间表示；
   单个字符评价非零确能推出原角点边界非零。
5. 正文 (17)–(19) 的裸加权非闭、对称链退化及提升 \(\alpha(K)\) 完整核验通过。
6. 正文 (20) 的实际 \(p\) 边缺陷也通过：置 \(E=He,V=HvH=vH\)，
   则 \(V^*V=E,VV^*=H(k-1)e\)；与 \(1-E\) 的交叉项为零，
   所以 \(T_p^*T_p=1,T_pT_p^*=1-\delta_{k=0}e\)，且端点 Green 投影非零。

最终限定 PASS。未发现需要阻止当前有限数学结论采纳的实质错误。
原源的完整循环／Chern 准入、规范理想类及全周期比较仍是实质未完成事项，
正文已准确保留这些范围限制。425 的不同候选不由这份复核自动认证。
