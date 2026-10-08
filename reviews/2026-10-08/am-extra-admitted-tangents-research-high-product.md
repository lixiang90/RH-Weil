# 从已准入点表增加完整区间有效切线

2026-10-08，high_product_joint；基线609fe754。
新结论是可复用的连续合同：原叶最多两个mixture点不限制epigraph可同时使用的有效点数。
原PTL任一点只要独立通过原tcheckPZ，就能加入完整区间切线。
本稿证明一个无需新核值／导数计算的直接REG分支，并在八个固定旧域上给精确有理增强。
没有准入更高全域奖励、新比例或新的纯Lean端到端定理。

canonical LF为UTF-8、CRLF/lone-CR→LF，保留EOF。

| 固定输入 | 身份 |
|---|---|
| 原Solution.lean | raw19049行／1675641字节／SHA012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f |
| [已准入有限抽取](../../scripts/am_pc8_finite_replay.py) | 复用483明确的192个PTL及REG准入；未重跑240项 |
| [当前epigraph程序](../../scripts/am_nine_point_epigraph_certificate.py) | 236／11009／af5f2e1974bed92ad515f06ff6047f3e5595ac60c6dc721abd7bfb5cfd930c32 |
| [当前全部原子与对偶](../../output/am-nine-point-epigraph-certificate.json) | 68844／1112534／0733022044f96b37c6be3d5d5c1e9fa6c269545142d7d535e643c835a7cf38f6 |

本轮完整读原PTF/ptl_sound、REG/chainOk_sound、ext_tangent、
tcheckPZ/tangent_valZ、mokZ/mterm_okZ/mokTZ/mtermTZ的相关完整定义与证明。
没有声称本轮逐行重读19049行、巨大mcheckP或重新认证旧点表。

## 1. 每个点的独立连续语义

令SC=32768，E=10⁹。原PTF f担保每个整数p的pack：
\[
 V/10^{10}\le w(p/SC),\qquad
 d_-=(P-2E)/E\le w'(p/SC)\le(2E-M)/E=d_+,\quad w=K_{\rm AM}^2.
\]
这是点值和点导数，单独并不担保整区间切线。
原tangent_valZ（Solution12217–12331）另给如下准确合同：
在原LBSound、LBSoundD、PTF和rgOk前件下，对任意n>0，
\[
 {\tt tcheckPZ}(REG,TOP,BK,n,L,U,p,f(p),{\tt treadU},{\tt treadD})={\tt true}
 \Longrightarrow {\tt TVal}(f,L,U,p).
\]
即L≤p≤U及整个真实闭区间上
\[
 w(x)\ge V/10^{10}+w'(p/SC)(x-p/SC),\quad L/SC\le x\le U/SC. \tag{1}
\]
该定理没有最多两点或固定旧mixture权的前件。
mokZ只为旧mterm计算选择两个点；新增epigraph行应逐点认证，不能借未启用点的旧mok返回值。

192个已准入PTL共有2196项，全部point不同，p范围27136…494592。
每个PTL分别由ptl_sound给PTF；可保留原列表编号使用对应f，所有f仍描述同一个w。
无需假设把不同列表拼成新函数后已经有PTF，也没有生成新的核pack。

## 2. 直接REG分支：纯整数认证完整区间

对候选p令k=(p+16384)>>15，A=rgA(REG,k)、B=rgB(REG,k)。
固定实际叶span整数端点L≤U，取
\[
 L^*=\min(L,p),\qquad U^*=\max(U,p).
\]
若逐项整数核验
\[
 k<16,\quad A\le L^*\le p\le U^*\le B,\qquad P\ge1,\ M\ge1, \tag{2}
\]
则原tcheckZ的两个extension条件分别由U*≤B、A≤L*直接为true。
其余rounding、point-in-region和point-in-query条件都在(2)中；
故原tcheckPZ在n=1时准确为true，毋须计算treadU/treadD或任何zside采样。
若L*=U*=p，tcheckPZ的单点分支只要求P,M≥1，同样为true。
于是(1)在整个[L*/SC,U*/SC]成立，限制回真实[L/SC,U/SC]。
REG准入担保整凸段kD<0及w''≥0，不能用浮点曲率或“接近整数”代替(2)。

本轮解析的全部2196个原点均落在其上述rounding所选REG段且P,M≥1；
给某叶加点仍须检查该叶实际L,U是否也包含于同段，不能一次性把所有点加到所有叶。
真实零宽span使用U=L；原uc=max(U,L+1)只服务旧constant lb查询。
不得把uc当成新增tangent的实际端点，或用扩大值查询推断扩大切线有效。

## 3. 有限盒可同时消费全部有效点

记v=V/10¹⁰、q=p/SC。对任何已认证点，若[J₋,J₊]包含q且在认证区间内，
对每个真实x∈[J₋,J₊]，两条独立安全线为
\[
 a_L(x)=v+d_+(J_--q)+d_-(x-J_-),\quad
 a_U(x)=v+d_-(J_+-q)+d_+(x-J_+). \tag{3}
\]
令d=w'(q)，原切线减a_L为
(d−d₋)(x−J₋)+(d₊−d)(q−J₋)≥0；
减a_U为(d₊−d)(J₊−x)+(d−d₋)(J₊−q)≥0。
因此同一真实z=w(x)同时满足每个认证点的两行z≥a_L、z≥a_U。
没有旧mixture加权限制；新增行保持真赋值可行，最强有效下界可同时消费。

共同closure若将真实x收紧到[a,b]，取J₋=min(a,q)、J₊=max(b,q)即可重新锚定；
其仍在原认证区间，不须重新核值。若q≤a，单线v+d₋(x−q)合法；
若q≥b，单线v+d₊(x−q)合法。
跨q时只有v+min{d₋(x−q),d₊(x−q)}是直接下界；
不允许把min误改max后无条件加入两条斜率线。
若要消费该分段更强线，必须以x≤q/x≥q的闭分支覆盖真实域。

无论选点来自浮点primal定位或确定列表，最终逐点(2)和完整有理残量才是证明。
对Ax≤b、盒[lo,hi]、任意λ≥0，r=c+Aᵀλ，严格用
\[
 c^tx\ge-\lambda^tb+\sum_i r_i(lo_i\ \text{若 }r_i\ge0;\ hi_i\ \text{若 }r_i<0). \tag{4}
\]
新增点不是独立物理变量；所有帧同一距离共用一个z。奖励、压力和索引预算均未更改。

## 4. 八个旧闭域的实际精确增强

隔离程序只选当前289报告中旧lower最小的八对，不执行上游大搜索。
每个新增行按(2)认证，LP仅提议非负乘子；舍入至10⁻⁹后依(4)用Fraction支付全部残量。
实际运行exit0（约6秒），原输入字节未改。下表的小数仅表示已经存下的有理lower。

| 来源标签 | 旧lower | 新有理lower的小数 | 正新增dual行 |
|---|---|---|---|
| 112／42 | .00805118280784758 | .008053144989764905 | 22 |
| 59／129 | .00805128015224718 | .008052679621116228 | 32 |
| 59／130 | .00805173941125465 | .008052874983730057 | 27 |
| 60／129 | .00805173941125466 | .008052902422270481 | 26 |
| 49／112 | .00805174908116448 | .008052609527750186 | 28 |
| 42／119 | .00805174908116453 | .008052609527750195 | 28 |
| 125／21 | .00805175687381390 | .008053006175840557 | 30 |
| 91／55 | .00805175789852207 | .008052980299548975 | 28 |

112／42的准确新lower是65971363756154106580552826643／8192000000000000000000000000000。
其新增13912行中正dual只用22行，可压缩到这些真正认证点，不需保存全部零乘子行。
这些是整个固定闭域的下界，不是采样点值；只八域不冒称当前全部289或新低集全付款。
更高δ仍须完整重捕F₈<c₀+2δ、保留新增叶、认证全部新拼接，再重付全零点运输。

忽略scratch：tmp/pdfs/am-more-tangents-high/，无Git或旧冻结修改。
convex_candidates.py完整读后执行；convex-candidates.json全部metadata、70候选计数、
八份有理lower、全部非负dual及所用原点已结构完整读回。
脚本156／6790／SHA bd965b07185bc3387ddc2158af88592b4e3040fd40f5d17f404bd3e68767fbaa；
JSON3922／63014／SHA f109bbee6e836c63015d967255197d7b9e539795ad287f2c55d34f498c79c83f。
程序复用已全文读取的236行矩阵与残量helper；它是本作者研究定位，不是不同作者审查。
完整连续合同保持原PC8准入信任范围；本稿不把LP、有限JSON或点导数变成新比例前件。
