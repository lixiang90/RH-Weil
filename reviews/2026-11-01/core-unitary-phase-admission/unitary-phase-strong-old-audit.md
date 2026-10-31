# 单一 Euler 相位的强旧与源角色审计

2026-11-01；/root/unitary_core_old_audit。独立准入审查，非新数学合同。已恢复Goal/STATE/check→show、macro22、D20261101I、C069原责任；现场STATE为惰性首检失败后的C069 stopped、cadence0/history70/latest606/formal22。本文不验收父线程工具会话，不改Goal/STATE/计数或执行任何科学代码。只审A_X/conj A_X这一候选，无参数或来源队列。

**裁决：INPUT0／标准强旧扣除后停止。** 同一卷积源槽上的酉相位不给新完整Weil型；若把它放在不同native坐标再读physical源，所需目标运输不能由前一事实代付。下述分别成立的事实不拼成更强的全类边界。

## 1. 明确对象和已付最强旧

采用Ff(t)=∫f(u)e^(-itu)du、dt/(2π)，T_a f(u)=f(u-a)。对每finite X≥2，
A_X(t)=∏_(p≤X)(1-q_p e^(-ita_p))，q_p=p^-1/2，a_p=logp；
U_X=F^-1 M_(A_X/conj A_X) F。
因q_p<1，每有限乘积无实零，U_X为全线L²(du)的酉算子，且保持全线Fourier log权型。它不自动保持compact支撑或S_exp。

旧017的BI早有局部酉平移平方恒等式及完整signed P−V接口；其中旧arch half-normalization须按其开头纠错处理，本文不消费旧half常数。590已经严分inverse-Euler的B、完整Gram逆、原源与非local运输，不把B当酉。591的共同occupation三测试定理有R≤Π前件；594的HS退耦有prime-linear ordinary-trace自伴前件。当前scalar相位乘子及其有限窗压缩尚未被证明属于这些类，不能直接拿591/594作总禁令。

更直接的旧资产是2026-10-30 Euler-inner/Clark原件及root消费：令
b_p(t)=(e^(ita_p)-q_p)/(1-q_p e^(ita_p))，B_X=∏b_p，
theta_X=∑_(p≤X)logp，则逐因子精确有

    B_X(t)=e^(it theta_X) U_X(t)。

因此U_X的中心化phase导数就是旧原件已明确保存的signed primepower数据：

    ψ'_X(t)=2∑_(p≤X,k≥1)logp·p^(-k/2)cos(klogp t)。

没有新的mixed arithmetic系数或独立正号由这次改名产生。但也不能把旧B_X的Schur/Clark平坦极限直接移给U_X：e^(-iz theta_X)在上半平面增长，U_X只是边界酉，非该上半平面的有界Schur inner。其signed导数不是正Clark权；完整目标仍需原Γ/contact、proper powers的负方向及indefinite双pole。

## 2. 必须保留的两个源槽解释

537 §2逐字固定F(z)=∫f e^(-izu)、h_f(x)=∫f(v+x)conj f(v)dv、Q_W(f)。560 §1则把实际卷积源记为r，并以hat r、A_r、R_r写完整Weil身份；576/577也明确B_W(r,s)=W(r*s*)。晚期C069又把native f-du与r=e^(u/2)f的weighted readout并列。不能靠同一个字母把这些位置合并，也不据此宣告历史定理整体矛盾。

(A) 若U_X作用于实际普通卷积源z（537的f，或在560公式中确实占据那个源槽的变量），则对全部L²源z,w和全部a，

    h_(Uz,Uw)(a)=<T_-a Uz,Uw>=<T_-a z,w>=h_(z,w)(a)。

Fourier产品属于L¹，所以上式是实际连续相关函数的等式；若输入compact smooth，右边就是原compact smooth测试。故完整Wζ作用于该相关函数时严格不变，Γ/contact、全部pp及双pole一并不变。这是标准Plancherel/平移交换的旧推论，不是新signed比较。自然Gram也精确等于原du内积。若把physical型明确定义为Q_phys[r]=Q_537[e^(-u/2)r]，那么相应共轭运输下同样只是这一旧型不变；这里使用的是这一定义，非另行识别560的ordinary r相关。

(B) 若严格坚持候选作用native f，但目标另取ordinary physical r=e^(u/2)f的Wζ(r*r*)，则须使用V_X=M_(1/2) U_X M_(-1/2)。其单prime精确规则是

    V_p=(I-T_a)(I-p^-1 T_-a)^-1
       =-T_a+(1-p^-1)∑_(k≥0)p^-k T_-ka。

它只在∫e^-u|r|²du这个weighted norm中由U继承酉性；在ordinary r-du中不是酉，不能据(A)声称h_(Vr,Vs)=h_(r,s)。原Γ/prime/pole目标的运输与sign defect仍欠。**(A)不能替(B)关闭根前提。**

全线U的满射也仅是L²满射，非原compact/S_exp或指定Weil型域的覆盖。只有另证同一完整型域的双向运输，才能用换元谈正性等价；这种等价本身亦不是独立正性来源。

## 3. 域、压缩和实际便宜首检

非compact不等于所有Weil配对都非法。对单prime，
U_p f=-qT_a f+(1-q²)∑_(k≥0)q^kT_-ka f。
取非负compact bump且支撑宽<a，通常∫U_p f·e^-u/2发散，而另一pole矩为0；不许把形式0×∞当pole已消失。但(A)的相关函数仍精确等于旧compact h，相关函数定义的完整W配对完全合法，只是旧Q。

在(B)，finite-X的V_X对compact smooth输入可得到指数尾费用：每0<γ<1的weighted绝对shift质量逐prime不超过
p^γ+(1-p^-1)/(1-p^(γ-1))，有限乘积有限。取γ>1/2可支付相关函数尾、全部Λ(n)/sqrt(n)和双pole配对的直接延拓；费用依X，输出一般不在原S_exp。本文不把这一可能的有费延拓升为uniform-X／growing-I费用、原全强域或新正性。

设R_(X,I)=1_I U_X 1_I、L_(X,I)=(1-1_I)U_X1_I。标准恒等式仅给

    R*R=I-L*L≥0，||R||≤1。

这支付一个正Gram与前向范数，不支付range满覆、逆费、完整Weil符号或core/cross。最便宜现成负对照不需数值：旧560全Γ给固定compact单位源的高频调制Q_W(r_T)~log|T|。未缩放Gram始终≤||f||²；在固定I=(-L,L)，||f||²≤e^L||r||²，故仍是T无关的上界。先固定一次足够大的T，便知该有界Gram不可能作为全部fixed源的完整Weil逼近。不得把这个结论扩大到未提出的成长scalar、signed修补或不同生成规则。

## 4. 根消费范围与止点

本次独立实物是一个明确有限Euler相位公式；便宜首检是同源相关函数/Clark phase强旧扣除和自然Gram的现成高频反测。它没有给新principal载体、全405关系下降、sections/mixed RR或有利成长core输入。物理槽按(B)解释时，目标运输/符号前提未付；不能把“还有该未付箭头”改名为已准新合同。

建议一次INPUT0停止，不运行source/Gram、不建C070、不续clock/phase/rank/sourcepaper。原whole17/16、fixed9/8头部和同605头全部补空间正完成、whole4/5负惯性UPPER均不变；whole9/8/core/growingΞ和三Goal门仍open。此为准入与语义审查，不是所有normal/unitary模型的边界，也不自行增加607或重置cadence。

实际阅读范围：017全文（仅BI/结构分层消费）、590/591/594及必要尾段、537 §2、560 §§1–4；旧Clark actual-inner-generator §§2–3、§6相关行和strongest-old §§2–4/root收据。未重审其nested外部原文，未使用新web/primary/PDF或数值。

源定义及旧消费的实际raw绑定（版本识别，非nested证明重审）：

| 文件 | bytes | SHA256 |
| --- | ---: | --- |
| notes/537-source-exact-weil-window-positive-tail-admission.md | 8155 | 269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8 |
| notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md | 9263 | 9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3 |
| notes/576-fixed-elliptic-positive-cone-and-original-alias-cost.md | 15924 | cbf32034c1e63518ef124ba89e1a46093b55da1086868532d8e5a1e0576595bd |
| reviews/2026-11-01/retained-tail-whole-admission/selected-whole-certificate.md | 9364 | 0328afa478fce4f73873776dc22e702f849233468f3afad09fc2d078a0a98ea7 |
| reviews/2026-10-30/euler-inner-clark-admission/root-consumption-scope.json | 7526 | 2171a2fea2e3f80058eb0340ba4d94267473e8c83d24deae6e0933d99fb04f9d |
