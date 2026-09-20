from pathlib import Path
import mpmath as mp,json,sys,sympy as sp
sys.stdout.reconfigure(encoding='utf-8')
mp.mp.dps=70
def eta(t):
 z=mp.pi*t*t
 return z*(z-mp.mpf('1.5'))*mp.exp(-z)
def eta00(t):
 z=mp.pi*t*t
 return (4*z**4-28*z**3+41*z**2-9*z)*mp.exp(-z)
def profile(x,fn):
 if x<0:return mp.exp(-x)*profile(-x,fn)
 lam=mp.exp(x)
 return 2*sum(fn(n*lam) for n in range(1,13))
def vm(n):
 fac=sp.factorint(n)
 return mp.log(next(iter(fac))) if len(fac)==1 else mp.mpf(0)
def N(fn):
 h0=profile(mp.mpf(0),fn)
 primes=sum(vm(n)*profile(mp.log(n),fn) for n in range(2,13))
 def integrand(x):
  if abs(x)<mp.mpf('1e-65'):return mp.mpf('.75')*h0
  return (mp.exp(2*x)*profile(x,fn)-h0)/mp.expm1(2*x)
 arch=mp.quad(integrand,[0,mp.mpf('.1'),mp.mpf('.5'),1,2,3])
 arch+=h0/2*mp.log1p(-mp.exp(-6))
 return primes+arch+(mp.log(mp.pi)+mp.euler)/2*h0
z=sp.symbols('z');P=z*z-sp.Rational(3,2)*z
A=lambda P:sp.expand(2*z*(sp.diff(P,z)-P))
p00=sp.expand(A(A(P))+A(P))
assert p00==4*z**4-28*z**3+41*z*z-9*z
result={'status':'exploratory_noninterval_check','precision_digits':70,'sum_cutoff':12,'archimedean_cutoff':3,
'exact_subtraction_tail_included':True,'omitted_Gaussian_tails_not_interval_certified':True,
'Euler_polynomial':str(p00),'N_theta':str(N(eta)),'expected_N_theta':'1/4','N_theta_degree_zero':str(N(eta00)),
'exact_result_method':'Mellin integral and gamma recurrence in the research proof; these quadratures are diagnostics only'}
p=Path(__file__).resolve().parents[1]/'reviews/2026-09-20/f1-theta-moment-numerical-check.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
