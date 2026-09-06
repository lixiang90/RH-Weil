# 335. 固定物理cell及determinant的精确整数纤维

2026-09-07。周期8第1动作及第2动作的初步分层。[T候选，独立复核待完成]。
先恢复旧MOM实验的同一实际算术对象；本篇没有获得相关和的新估计。

## 1. 固定对象，不改变中心化或窗口

采用240–241配套脚本[mobius_divisor_pullback_audit.py](../scripts/mobius_divisor_pullback_audit.py)
已有的balanced平窗cell。X为充分大正整数，L=log X，Y=X^(3/4)，
I_X=[ceil(.70Y),floor(1.30Y)]，D=round(XL)，M=X^(1/2)。
这只是原MOM全局账本中的一个平窗测试cell，不等于已覆盖所有cell或已换成sharp MT窗。

对prime-power a,b in I_X，要求其素数底不同，令
q_ab=Lambda(a)Lambda(b)/(4pi²sqrt(ab))，s_ab=log(a/b)。
其平窗支持区间为
\[
 J_{ab}=[\log a-L/2,\ L/2+\min(0,s_{ab})].
\]
对充分大X此区间长度为正且小于L。将其示性函数L周期延拓为P_ab，
保留准确的六窗重叠
\[
 W_{ab;cd}={1\over L}\int_{-L/2}^{L/2}
               P_{ab}(u)P_{cd}(u-\Delta)\,du,\quad
 \Delta=\log(ad/bc).                                    \tag{1}
\]
这里是既有flat_support/periodic_shifted_overlap的数学定义，
不是把W改成1或丢掉某些窗口。W_{ab;cd}=W_{cd;ab}。

令
\[
 K_X(t)={1\over D}\sum_{k=0}^{D-1}
             \cos(2\pi(1+k/(XL))t),\qquad
 \bar K_X(M)={1\over M}\int_0^M K_X(t)\,dt.              \tag{2}
\]
于是同一脚本的直接中心响应精确为有序和
\[
 {\cal R}_X=\sum_{\substack{a,b,c,d\in I_X\\
   a,b,c,d\ {\rm prime\ powers}\\
   {\rm base}(a)\ne{\rm base}(b),\ {\rm base}(c)\ne{\rm base}(d)\\
   0<|\log(ad/bc)|\le M/X}}
 q_{ab}q_{cd}W_{ab;cd}
       \{K_X(X\log(ad/bc))-\bar K_X(M)\}.                 \tag{3}
\]
脚本对ratio排序后只取无序对再乘2，与(3)一致，因为K为偶函数及W对称。
中心项先前已固定为同一shell平均，不能为方便Kloosterman变换另行选择。
去掉的是全部determinant=0项，不仅仅是(a,b)=(c,d)的原子对角。

式(3)仍有全部四个Lambda权。若继续Vaughan展开，沿用脚本固定的整数mask：
在Lambda(a)=0时保留原已选的extension；不能因新通道而改mask或遗漏ghost。

## 2. 逐个determinant的精确参数化

记h=ad-bc，g=gcd(b,d)，b=g b'、d=g d'，gcd(b',d')=1。
无解情形恰包含g不整除h。若g|h，写h'=h/g，
取唯一a0 in {0,...,b'-1}满足
a0 d'≡h' (mod b')；b'=1时a0=0。
令c0=(a0 d'-h')/b'，它是整数。则所有整数解精确为
\[
 a=a_0+b't,\qquad c=c_0+d't,\qquad t\in{\mathbb Z}.       \tag{4}
\]
证明：任一解的a满足该同余，所以a-a0=b't；代回即给c-c0=d't。
反向代入直接得到ad-bc=h。这里没有近似、平均或互素项丢弃。

因此(3)可在固定b,d,h上对(4)的t求和，所有原权、mask、
六窗与K_X(X log(1+h/(bc)))都在该同一t上保留。
特别是Lambda(a0+b't)Lambda(c0+d't)尚未变成平滑权或任意可优化系数。
中心项和h=0的删除随同一参数化保留。

因|Delta|<=M/X=X^-1/2、bc<=1.69Y²，
\[
 |h|\le1.69Y^2(e^{X^{-1/2}}-1)\ll X.                   \tag{5}
\]
这是一整个当前中心shell的determinant范围。单个主振荡尺度
X|Delta|=O(1)才对应|h|=O(Y²/X)=O(X^1/2)；
两者不得混写，不能仅估计后一范围后宣称处理了(3)。

## 3. 固定互素分母的纤维不是平方根长自由和

由a,c均在长度<=.60Y+1的I_X内，允许的t位于两个实区间的交集，
总长度至多
\[
 { .60Y+1\over\max(b',d')}
 \le {(.60Y+1)g\over .70Y}=O(g).                        \tag{6}
\]
所以每个固定b,d,h的整数t只有O(g+1)个。
当b,d是不同素数底的prime powers，g=1，这条纤维只有O(1)个点；
若b,d同底，g可能很大，该分层不能舍掉。
式(3)的pairwise distinct-base mask不要求base(b)与base(d)不同。

这说明：仅固定b,d,h并使用(4)，尚未得到Pascadi/MQW的
长度约sqrt(q)的两条自由变量和。取q=bd的字面替换没有生成完整Kloosterman核。
这不是对进一步变换的否定：可以在h、分母或Vaughan后的自由补全变量上继续求和，
但必须连同原始系数和六窗建立真正的完整核及长度账本。

下一动作是检查这些合法求和次序中哪一个能接合
[新原始条款](../reviews/2026-09-07/kloosterman-next-input-screen.md)，
先给可审计变换，尚不对原响应声称o(L^4)或算术净收益。
