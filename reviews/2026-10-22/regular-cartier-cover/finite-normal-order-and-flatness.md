# 实际螺旋覆盖：非flat Cartier代表的精确指数门

2026-10-22，root独占推导，供C038独立审查。固定574实际覆盖，不读取完整Q或Ξ零点；不宣称外部首创。
连续／smooth Cartier实现见[natural原件](natural-sheaves-and-cartier.md)，实际源及费用见[source原件](actual-source-map-and-costs.md)。

## 1. 层、normal jets与方向先固定

L=log2，M=log3；两side商Z_L、Z_M分别嵌入圆柱[0,∞)×S¹：
`x↦(ρ,θ_L)=(e^x,e^(2πix/L))`，负端补整个ρ=0圆。Γ、O、Wp/Wq及共同bulk坐标全部沿413/574。
在每side取局部为ambient C∞函数限制的复值函数层S∞。bulk上为通常x-smooth函数；此层在bulk重合，可沿真实开覆盖作等变粘合。
这是由指定ρ圆柱选出的候选层，不是从裸g分布唯一恢复的scheme／DVR。

边界紧性允许在一个共同小圆柱内用ambient smooth partition of unity统一局部延拓。其normal Taylor系数是圆上的smooth函数。
这些系数不依赖延拓：若两个延拓在螺旋上相同，差F满足F(e^x,θ_L(x))=0。
先令x=x₀−nL→−∞，得到F(0,θ_L(x₀))=0；假定前m个系数已为0，除ρ^m再取同一列，得到第m系数也为0。
故全部normal jets独立；不声称整个ambient函数独立，flat差仍可存在。

称side函数flat，意为所有normal Taylor系数在**整个边界圆**恒为0；等价于其bulk值对每个N一致为O(ρ^N)。
一个方向由统一Taylor余项给出；另一个方向由首个非恒0 Taylor系数和上述周期列排除。
这里不是只在一个角度无穷阶消失，也不假定每个点的阶相同。

以下Cartier型数据指局部由结构层非零因子生成的等变可逆理想。取局部生成元h_p、h_q，约定

\[
h_p=e^{zx}h_q\quad\text{在共同bulk},\qquad z=a+i\lambda.\tag{1}
\]

因此理想frame满足e_p=e^(zx)e_q，I=O(−D)对应574的L_z；通常O(D)=I^∨，canonical regular截面的系数为h_p、h_q。
这一区分不影响指数核，却影响section／ideal的消费方向。
可先限定h_p、h_q在bulk无零以保证regular性；下面必要性只用(1)及各side smooth性，不擅自分类所有Cartier/Pic对象。

## 2. 命题：非flat门准确为Z+iΛ

记Λ=(2π/L)Z+(2π/M)Z。对(1)的side函数，有：

**命题。** 若有一个side不是flat，则两个side都不是flat，且

\[
z\in\mathbb Z+i\Lambda.\tag{2}
\]

反过来，每个z∈Z+iΛ都有bulk无零、两个side均有有限normal首项的smooth regular方程实现。
对任意其他z，任何属于上述类型的smooth Cartier方程对只能两边同时flat。

### 2.1 先排“一边flat、另一边不flat”

由(1)，|h_p|=ρ^a|h_q|。固定a有限，乘一个ρ实幂保持“对任意N为O(ρ^N)”的值flat性。
§1的Taylor等价把它变为两侧同时normal-flat。因此只要一边有首项，另一边也有首项。
这一论证不把ρ^z本身误当作可延到边界的unit。

### 2.2 不预设首项无零，先比较实阶

设m,n≥0为两side首个在整个圆上不恒0的normal Taylor阶，A、B为首系数的周期提升。统一Taylor展开给

\[
h_p(e^x)=e^{mx}[A(x)+O(e^x)],\quad
h_q(e^x)=e^{nx}[B(x)+O(e^x)],\qquad x\to-\infty,\tag{3}
\]

A是L周期、B是M周期，均连续且不恒0，暂时允许有零点。
设δ=a+n−m。若δ>0，(1)(3)迫A(x)→0于整个负尾；周期性迫A≡0，矛盾。
若δ<0，反向相除实幂后迫B(x)→0，同样矛盾。因此

\[
a=m-n\in\mathbb Z,\qquad
e^{i\lambda x}B(x)-A(x)\longrightarrow0\quad(x\to-\infty).\tag{4}
\]

这里仅用A、B有界和统一O(e^x)；没有在可能的零点处先除以A或B。

### 2.3 负尾恒等、零点传播与绕数

574已付的紧三频环面近回归序列t_j→+∞，使λt_j、2πt_j/L、2πt_j/M同时模2π趋0。
把(4)作用于任意固定x−t_j，用周期函数的一致连续性得

\[
A(x)=e^{i\lambda x}B(x)\quad\forall x\in\mathbb R.\tag{5}
\]

若B(x₀)=0，M周期性与(5)使A(x₀+kM)=0对全部整数k成立。
M/L无理，故这些点在L圆上稠密；A连续遂恒0，矛盾。若A有零点，(5)先给B同点为0。
因此两首系数**自动都是无零周期unit**。这一步补上“首系数可能在某些角度消失”的缺口，不能直接以unit-leading旧推论替代。

取它们的绕数u,v，写

\[
A(x)=e^{2\pi iux/L}e^{\alpha(x)},\qquad
B(x)=e^{2\pi ivx/M}e^{\beta(x)},
\]

α、β为有界周期log。(5)的提升差为常数2πi整数，有界性迫λ=2πu/L−2πv/M∈Λ。
结合(4)即得必要性(2)。

### 2.4 充分性与有效范围

若z=k+i(2πu/L+2πv/M)，选m,n≥1且m−n=k，取

\[
h_p=\rho^m\theta_L^{u},\qquad h_q=\rho^n\theta_M^{-v}.\tag{6}
\]

两者ambient smooth、bulk无零、各边界首项为unit，交比精确为e^(zx)。各side的bulk稠密，乘h无核；故确有regular Cartier型理想。
正阶m,n也使两侧都属于有效方程。这不是只给出必要条件。

命题只比较指定ρ-normal结构、相同两片和固定指数clutch；不分类一般moving支集、额外normal方向、非scalar相对层或全Pic。
保boundary frames不改变(1)的方程比较，但iΛ中的framed非平凡类仍可用(6)实现；不能从absolute平凡推出relative平凡。

## 3. 所有z仍有smooth Cartier：必须保留flat修补

取E(ρ)=exp(−1/ρ²)、E(0)=0。对任意z∈C，

\[
h_p=E(\rho)\rho^z,\qquad h_q=E(\rho)\tag{7}
\]

均ambient smooth且所有normal jets为0，bulk无零，交比仍为e^(zx)。参数z在任意紧集上连同全部混合导数一致flat，给真实联合smooth族。
故(2)不等于“其他z没有Cartier”；它判的是finite-normal首项。

特别纯虚且absolute非平凡的574类（λ∉Λ）可以Cartier化，却**任何本门内的定义方程只能两侧flat**。
若把局部方程送到ρ-adic完备化，(7)在每阶都为0：除ρ^N仍smooth。
因此原来是非零因子的局部方程在这个完成化中变成0，regular截面／Cartier性不能无条件运输。
这是方程及其嵌入的损失；不是证明整个线丛、形式Pic群或一般formal/derived修补都为零。

### 3.1 共同正实幂换坐标的已付修补

若两side共同改用τ=ρ^c、固定c>0定义ambient smooth normal结构，同一证明把(2)的实部格改为cZ，虚部仍为iΛ：首项为e^(cmx)A、e^(cnx)B。
因而纯虚absolute非平凡类必须两边flat的结论不因这类换坐标消失。全部S_exp源的primitive在τ中仍flat，因为超指数界可取任意N。
这是每个固定c的范围，不报告关于c变化的统一metric费用，也不排不同normal方向／不同层或源依赖厚化。

## 4. 对物理源的意义：新增设施与未付责任分开

实际primitive源A_r(x)=∫_-∞^x r、r∈S_exp，令g_r=e^(A_r)。source原件已给全部normal jets(g_r−1)=0，g_r及逆却是真正side units且boundary为1。
所以它的clutch为relative coboundary；405全关系与537真非根都被消去。
若以h_p=E g_r、h_q=E构造Cartier理想，因g_r是同层unit，两边ideal均等于(E)：实际理想本身也不随源移动。
保留g_r作为mark会保raw源，但不是从Pic类或局部消失过滤获得的算术输入。

§2说明不能简单以“只保非flat normal首项”恢复非平凡unitary子族；§3又给合法flat有效代表，不能删掉它们后宣布全方法不可能。
换成真正解析／quasianalytic层可排非零flat germs，却须首先支付原S_exp域、405实际非compact关系、源lift及原范数；source原件已给相应具体失败范围。
需要的是独立自然层和非scalar／moving源桥的真实新数据，不是以旧Q或零点坐标指定剩余对象。

本命题不提供独立mixed容量、完整Γ/prime-power/pole预算identity、成长core或Ξ。
它补全574之后“非平凡线能否Cartier化、finite normal过滤能否承载其相位”的具体局部门；同C038统一一轮，不另计本文件。
