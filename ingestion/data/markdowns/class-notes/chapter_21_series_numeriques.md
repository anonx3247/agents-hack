# Chapitre 21: Séries numériques

Dans ce chapitre $(u_k)$ désigne une suite a valeurs dans $\mathbb{K}$

## Définition et premierres remarques

### Définition

#### Définition *Somme Partielle*

Soient $(u_k) ∈ \mathbb{K}^{\mathbb{N}}$ et $n ∈ \mathbb{N}$

- La somme partielle d'indice $n$ associée a la série de terme général $u_k$ est le scalaire:
$$
S_n = \sum_{k=0}^{n} u_k
$$

On dit que la série $\sum u_k$ converge si la suite $S_n$ converge.
Sinon on dit qu'elle diverge.

La notation $\sum u_k$ désigne la série de terme général $u_k$.

- Si $\sum u_k$ converge alors on note:
$$
\sum_{k=0}^{+\infty} u_k = \lim_{n\to+\infty} S_n
$$

#### Remarque "oubli des premiers termes"

La nature d'une série reste inchangée par la modification d'un nombre fini de termes.

C'est pour cela qu'il n'y a aucun problème si la série est définie a partir d'un certain rang $n>0$.

#### Définition *Reste d'une série convergente*

Soit $\sum u_k$ une série convergente. On appelle reste d'ordre $n$ associé a la série de terme général $u_k$ la scalaire défini par
$$
R_n = \sum_{k=n+1}^{+\infty} u_k
$$

#### Remarque
$$
S_n + R_n = \sum_{k=0}^{+\infty} u_k
$$

#### Théorème
Si $\sum u_k$ converge alors $(R_n)$ cnverge vers $0$

#### Preuve

$$
R_n = \sum_{k=0}^{+\infty} u_k - S_n \to 0
$$

#### Remarque

La réciproque est inintéressante car celle-ci n'a pas de sens.

### Une condition nécéssaire mais non-suffisante de convergence d'une série numérique

#### Théorème

Si la série $\sum u_k$ converge alors $(u_k) \to 0$

#### Preuve
$∀ k ∈ \mathbb{N}^{*}, u_k = S_k - S_{k-1} \to_{k\to+\infty} 0$

#### Définition *Convergence grossière*

Par contraposée, si $(u_k)$ ne converge pas vers 0, alors $\sum u_k$ diverge, et on parle de divergence grossière!

#### Remarque

La réciproque est fausse:
par exemple la série harmonique:
$$
\sum \frac{1}{k}
$$

Pour $n ∈ \mathbb{N}^{*}$:

$$
H_n = \sum_{k=1}^{n} \frac{1}{k}
$$

$$
H_{2n} - H_n = \sum_{k=n+1}^{2n} \frac{1}{k} \ge n \times 1/ 2n = \frac{1}{2}
$$


Si $(H_n)$ converge alors en passant a la limite dans l'inégalité précédente on obtient que $l-l > 1/2$

Donc $(H_n)$ diverge.

### Quelques exemples

#### Le critère des séries téléscopiques

#### Théorème

Soit $(w_k)$ une suite.
$$
\sum w_{k+1} - w_{k} \text{ converge } \iff (w_k) \text{ converge}
$$

Dans ce cas,
$$
\sum_{k=0}^{+\infty} w_{k+1} - w_k= \lim_{n\to+\infty} w_n - w_0
$$

#### Preuve

On a:
$$
\sum_{k=0}^{n} (w_{k+1} - w_k) = w_{n+1} - w_0
$$

Donc $\sum w_{k+1} - w_k = \lim w_{n+1} - w_0 = \lim w_n - w_0$

#### Exemple

Nature de la série
$$
\sum_{k\ge 1} \frac{1}{k(k+1)}
$$

$$
\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}
$$

Or $(\frac{1}{k}) \to 0$ donc $\sum \frac{1}{k(k+1)} \to \lim 1 - \frac{1}{n} = 1$

#### Exemple

Nature de:
$$
\sum_{k \ge 1} \ln \left(1 + \frac{1}{k}\right)
$$

$$
\ln \left(1  + \frac{1}{k}\right) = \ln (k+1) - \ln k
$$

Or $(\ln k) \to +\infty$ donc $\sum \ln (1 + 1/k)$ diverge grosièrement.

#### Le cirtère des séries géométriques

#### Théorème

Soit $q ∈ \mathbb{C}$,
$$
\sum q^{k} \text{ converge } \iff |q| < 1
$$

Dans ce cas:
$$
\sum_{k=0}^{+\infty} q^{k} = \frac{1}{1-q}
$$

#### Preuve

- Si $|q| \ge 1, \lim_{k\to+\infty}(q^{k}) \neq 0$

- Si $|q| < 1$ alors
$$
\sum_{k=0}^{n} q^{k} = \frac{1 - q^{n+1}}{1 - q} \to \frac{1}{1-q}
$$

#### Exemple

Nature de $\sum_{k \ge1 } 3^{-k}$

- $\frac{1}{3} < 1$ donc la série converge
- $\sum_{k=1}^{+\infty} 3^{-k} = -1 + \sum_{k=0}^{+\infty} 3^{-k} = -1 + \frac{1}{1 - 1/3} = \frac{1}{2}$

### Somme de séries convergentes

#### Théorème

Si $\sum u_k$ converge et si $\sum v_k$ converge, et si $λ , μ ∈ \mathbb{K}$

alors $\sum (λ u_k + μ v_k )$ converge et
$$
\sum_{k=0}^{+\infty} (λ u_k + μ v_k) = λ \sum_{k=0}^{+\infty} u_k + μ \sum_{k=0}^{+\infty} v_k
$$

#### Preuve
$$
\sum_{k=0}^{n} λ u_k + μ v_k = λ \sum_{k=0}^{n} u_k + μ \sum_{k=0}^{n} v_k
$$

On fait en suite tendre $n$ vers $+\infty$.

#### Remarque

- La somme de deux séries convergentes est convergente.
- La somme d'une série divergente et convergente est divergente.
- La somme de deux séries divergentes, on ne peut rien conclure.

#### Remarque

Pour passer de:
$$
\sum u_k + v_k = \sum u_k + \sum v_k
$$

Il faut vérifier qu'au moins une des séries converge.

### Lien avec les parties positives et négatives

#### Théorème

Soit $(u_k) ∈ \mathbb{R}^{\mathbb{N}}$,

Si
$$
\sum u_k ^{+} \text{ et } \sum u_k ^{-} \text{ convergent, alors } \sum u_k \text{ converge, et } \sum u_k = \sum u_{k}^{+} - \sum u_k ^{-}
$$

#### Preuve

$u_k = u_k^{+} - u_k^{-}$ donc deux séries convergentes, se somment en une série convergente.

#### Remarque

La réciproque est fausse,
$$
\text{Si } \sum u_k \to l
$$

Alors il n'y a aucune raison pour que $\sum u_k^{+}$ et $\sum u_k^{-}$ convergent.

#### Exemple

Étudions la nature de $\sum \frac{(-1)^{k}}{k+1}$ et de $\sum (\frac{(-1)^{k}}{k+1})^{-}$

$$
S_n = \sum_{k=0}^{n} \frac{(-1)^{k}}{k+1}
$$
$$
S_n = \sum_{k=0}^{n} (-1)^{k} \times \int_{0}^{1} t^{k} dt
$$
$$
S_n = \int_{0}^{1} \sum_{k=0}^{n} (-t)^{k} dt
$$
$$
S_n = \int_{0}^{1} \frac{1}{1+t} dt - \int_{0}^{1} \frac{(-t)^{n+1}}{1+t} dt
$$
$$
S_n = \ln(2) - ε _n / ε _n = \int_{0}^{1} \frac{(-t)^{n+1}}{1+t} dt
$$
$$
0 \le |ε _n| \le \int_{0}^{1} \frac{t^{n+1}}{1+t} < \int_{0}^{1} t^{n+1}dt = \frac{1}{n+2}
$$

Donc $ε _n \to 0$ et $S_n \to \ln(2)$,

$$
∀ k, u_k^{+} = \begin{cases}
0 \text{ si } k \text{ impair} \\
\frac{1}{k+1} \text{ si } k \text{ pair}
\end{cases}
$$

Montrons que $\sum u_k^{+}$ diverge

en montrant que $\sum_{k=0}^{n} u_{k}^{+}$ diverge.

Pour cela il suffit de prouver que la sous suite:
$$
\left(\sum_{k=0}^{n} u_k^{+}\right) \text{ diverge.}
$$

On a:
$$
\sum_{k=0}^{2n} u_{k}^{+} = \sum_{p=0}^{n} u_{2p}^{+} = \overbrace{\sum_{p=0}^{n} \frac{1}{2p+1}}^{\text{noté } S_n}
$$

On a:
$$
S_{2n} - S_n = \sum_{p=n+1}^{2n} \frac{1}{2p+1} \ge \frac{n}{4n+1}
$$

### Lien avec le conjugué, la partie réelle, la partie imaginaire

#### Théorème

Soit $(u_k) ∈ \mathbb{C}^{\mathbb{N}}$
$$
\sum u_k \text{ converge} \iff \sum \overline{u_k} \text{ converge}
$$

Dans ce cas,
$$
\sum \overline{u_k} = \overline{\sum u_k}
$$

#### Preuve

$$
\overline{a+b} = \overline{a} + \overline{b} \text{ et } \overline{\lim u_n} = \lim \overline{u_n}
$$

#### Théorème

Soit $(u_k) ∈ \mathbb{C}^{\mathbb{N}}$
$$
\sum \Re(u_k) \text{ et } \sum \Im(u_k)
$$
convergent,
si et seulement si
$$
\sum u_k 
$$
converge.

Dans ce cas
$$
\sum u_k = \sum \Re(u_k) + i \sum \Im(u_k)
$$

#### Preuve
$$
\lim \Re(z_n) = \Re(\lim z_n), \lim \Im(z_n) = \Im(\lim z_n)
$$

## Séries a termes positifs

#### Remarque

Soit $(u_k)$  une suite a valeurs dans $\mathbb{R}^{+}$

Dans ce cas:
$$
S_n = \sum _{k=0}^{n} u_k 
$$

verifie:
$$
∀ n ∈ \mathbb{N}, S_{n+1} - S_n = u_{n+1} \ge 0
$$

Donc $(S_n)$ est croissante.

Or si elle est majorée, elle converge, sinon, elle diverge en $+\infty$ 

#### Remarque

En réalité, tout ce qu'on dit dans cette partie fonctionne pour les series avec un terme général de signe constant a partir d'un certain rang.

### Les théorèmes de comparaison

#### Théorème

Soit $(u_k), (v_k)$ deux suites telles que:
$$
∃ N ∈ \mathbb{N} / ∀ k ∈ \mathbb{N}, (k \ge N \implies 0 \le u_k \le v_k)
$$

Si $\sum v_k$ converge,  alors $\sum u_k$ aussi.

#### Preuve

On pose
$$
S_n = \sum_{k=0}^{n} u_k
$$
et
$$
T_n = \sum_{k=0}^{n} v_k
$$ 

On a donc que comme $\sum v_k $ converge, $(T_n)$ converge donc $T_n$ est majorée, puis $(S_n)$ est majorée et donc converge, et enfin $\sum u_k$ converge. 

#### Exemple

Nature de:
$$
\sum \frac{1}{k^3}
$$
Or $0 \le \frac{1}{k^3} \le \frac{1}{k^2}$

et $\sum \frac{1}{k^2}$ converge, donc $\sum \frac{1}{k^3}$ aussi.

#### Théorème

Soient $(u_k), (v_k)$ deux suites, avec

- $v_k > 0$

- $u_k = \bigcirc_{k\to+\infty} (v_k)$

Si $\sum v_k$ converge alors $\sum u_k$ aussi.

#### Preuve
$$
∃ c ∈ \mathbb{R}^{+} / ∀ k ∈ \mathbb{N}, |u_k| \le c |v_k|
$$
$$
∃ c ∈ \mathbb{R}^{+} / ∀ k ∈ \mathbb{N}, |u_k| \le c v_k
$$

Or $\sum v_k$ converge donc $\sum u_k$ converge (théorème précédent)
Donc $\sum u_k$ converge.

#### Théorème

Soient $(u_k), (v_k)$ deux suites, avec 
$$
u_k = \circ_{x\to+\infty} (v_k)
$$

#### Exemple

$$
\sum \frac{k^2}{3^{k}}
$$
$$
\frac{k^2}{3^{k}} = \circ_{x\to+\infty} (\frac{1}{k^2})
$$

donc $\sum \frac{k^2}{3^{k}}$ converge.

#### Exemple

Nature de:
$$
\sum \frac{1}{k \ln k}
$$
$$
\frac{1}{k \ln k} = \circ (\frac{1}{k})
$$

or $\sum 1/k$ est divergent

#### Théorème

Soient $(u_k), (v_k)$ deux suites, avec 
$$
v_k >0
$$
$$
u_k \sim v_k
$$
 
Et $\sum u_k$ converge si et seulement si $\sum v_k$  converge

#### Preuve

$\impliedby$ 
On suppose $\sum v_k$ convergente, et $v > k$

On a:
$$
u_k = v_k + \circ(v_k)
$$

Or $(v_k)$ converge donc $u(k)$ aussi.et $\sum o (v_k)$ converge, comme somme de 2 séries convergentes:

$\implies$
Par symmétrie des roles de $u$ et $v$ on a le reste.

#### Exemple
$$
\sum \sin \frac{1}{k}
$$
$$
\sin \frac{1}{k} \sim \frac{1}{k}
$$
or $\sum \frac{1}{k}$ ne converge pas donc ici non plus.

Donc $\sum \sin \frac{1}{k}$ est divergente.

#### Exemple
$$
\sum \arctan\frac{1}{k^2}
$$

$$
\arctan \frac{1}{k^2} \sim \frac{1}{k^2}
$$

Or $\sum \frac{1}{k^2}$ tend vers qq chose donc $\sum \frac{a}{k^2}$

#### Théorème

Il existe $(u_k), (v_k)$ deux suites, avec $u_k$ convergente  et $v_k$ divergent.

- $u_k \sim v_k$
- $\sum v_k$ converge
- $\sum u_k$ + divergence.

### La regle de d'Alembert

#### Théorème

Soit $(u_k)$ une suite strictement positive, on suppose qu'il existe $l ∈ \mathbb{R}^{+} \cup \{\pm \infty\}$

- $l = 1^{+}$ ou $l > 1 \implies \sum u_k$ diverge
- Si $l < 1, \sum u_k$ converge
- si $l = m$ on peut rien conclure.

#### Preuve

- Si $l = 1^{+}$ ou $1  = m, \text{ ou }, $n-k > γ ∈ G$
- Donc $u_k$ est croisssante a partir d'un rang, donc elle converge.


- Si $l < 1/q,q_0 ∈ ]l,1[.$ A partir d'un certain rang, on note $k_0 = \frac{u_{k+1}}{u_k} \le q$

Donc $∀ k \ge k_0  , \frac{u_{k+1}}{u_k}$

Par récurrence immediate on a:
$$
u_k \le q^{k-k_0} \times u_{k_0}
$$

Or $q < 1$ donc $\sum q^{k}$ converge et $\sum u_k$ converge.

si $l = 1$

#### Exemple
$$
\sum \frac{1}{k!} > 0, \frac{u_{k+1}}{u_k} = \frac{1}{k+1} \to 0 < 1
$$

Donc d'apres d'alembert elle converge.

### Comparaisons séries-intégrales

#### Théorème

Supposons donné $f$ continue sur $\mathbb{R}^{+}$ a valeurs réelles, positive et décroissante, on peut montrer que:
$$
\sum f(k) \text{ converge } \iff \int_{0}^{n} f(t)dt \text{ converge }
$$

La nature de la série $\sum \frac{1}{k \ln k}$

$f: t \mapsto \frac{1}{t \ln t}$

$f$ est continue sur $[2, +\infty[$, positive, et décroissante, donc:
$$
\sum \frac{1}{k \ln k} \iff \int_{2}^{n} \frac{1}{t \ln t} dt
$$

$$
\int_{2}^{n} \frac{1}{t \ln t} dt = [\ln \circ \ln (t)]_{2}^{n} = \ln \circ \ln n - \ln \circ \ln 2 \to + \infty
$$

Donc $\sum \frac{1}{k \ln k}$ diverge.

#### Preuve

$$
\int_{k}^{k+1} f(t) dt \le_{(1)} f(k) \le_{(2)} \int_{k-1}^{k} f(t) dt
$$

$$
\int_{0}^{n+1} f(t) dt \le \sum _{k=0}^{n} f(k) \le \int_{-1}^{n} f(t) dt
$$
$$
\int_{0}^{n+1} f(t) dt \le \sum _{k=0}^{n} f(k) \le \int_{0}^{n} f(t) dt +f(0)
$$

Donc par encadrement, $S_n = \sum_{k=0}^{n} f(k) \to \lim_{n\to+\infty} \int_{0}^{n} f(t)dt$

1. On suppose que $(\int)$ converge et est donc majorée, puis
$$
S_n = \sum_{k=0}^{n} f(k)
$$
Est aussi majoré.
2. On suppose que $(\sum)$ converge et donc est majorée par $M$ 
puis
$$
\int_{0}^{n+1} f(t) dt \le M
$$ 

Comme $\int_{n+1} - \int_n = \int_{n}^{n+1} > 0$ et est croissante.
Donc
$\int$ majorée et converge.

#### Corollaire "Séries de Riemann"

Soit $α ∈ \mathbb{R}$
$$
\sum \frac{1}{k^{α }}
$$
converge si et seulement si $α > 1$

#### Preuve

Si $α ∈ \mathbb{R}^{-}$, $\left(\frac{1}{k^{α }}\right)$ ne converge pas vers 0

Si $α > 0$ alors pour $f: t \mapsto \frac{1}{t^{α }}$

$f$ est continue, positive et décroissante sur $[1, +\infty[$
$$
\int_{0}^{n} f(t)dt = \begin{cases}
[\frac{1}{1 - α }t^{1 - α }]_{0}^{n} \text{ si } α \neq 1 \\
[\ln t ]_{0}^{n} \text{ si } α = 1
\end{cases}
$$

donc quand $n \to +\infty$ on a:

$$
\lim_{n\to+\infty} \int_{0}^{n} f(t)dt = \begin{cases}
c ∈ \mathbb{R} \text{ si } α \neq > 1\\
+\infty \text{ si } α = \le 1
\end{cases}
$$

#### Exemple "Serie de Bertrand"
$$
\sum \frac{1}{k^{α } (\ln k )^{ β  }}
$$

Si $α < 1$:
$$
\frac{1}{k} = \circ \left(\frac{1}{k^{α } (\ln k )^{ β }}\right)
$$


#### Exemple: $\frac{π ^2}{6} = \sum_{k=1}^{+\infty} \frac{1}{k^2}$

$$
\frac{π ^2}{6} - \sum_{k=1}^{n} \frac{1}{k^2} = \sum_{k=n+1}^{+\infty} \frac{1}{k^2}
$$

soit $p \ge n+1$

SOit $k ∈ [[n+1,p]]$

$$
\int_{k}^{k+1} \frac{1}{t^2} dt \le \frac{1}{k^2} \le \int_{k-1}^{k} \frac{1}{t^2} dt
$$

$$
\int_{n+1}^{p+1} \frac{1}{t^2} dt \le \sum_{k=n+1}^{p} \frac{1}{k^2} \le \int_{n}^{p} \frac{1}{t^2} dt
$$

$$
\frac{-1}{p+1} + \frac{1}{n+1} \le \sum_{k=n+1}^{p} \frac{1}{k^2} \le \frac{-1}{p} + \frac{1}{n}
$$

$$
\frac{1}{n+1} \le \sum_{k=n+1}^{+\infty} \frac{1}{k^2} \le  \frac{1}{n}
$$

$$
\frac{1}{n+1} \le \frac{π ^2}{6} - \sum_{k=1}^{n} \frac{1}{k^2} \le  \frac{1}{n}
$$

## Séries a terme changeant de signe

### Convergence absolue

#### Définition *Convergence absolue*

On dit que $\sum u_k$ converge absolument (CVA) si  $\sum |u_k|$ converge.

#### Théorème

Si $\sum u_k$ converge absolument, alors $\sum u_k$ converge.

#### Exemple 

$$
\sum \frac{(-1)^{k}}{k^2}
$$

Converge car elle converge absolument

#### Preuve

##### Cas réel

$∀ k ∈ \mathbb{N}$, $0 \le u_k^{+}, u_k^{-} \le |u_k|$

Or $\sum |u_k|$ converge donc $\sum u_k^{+}$ et $\sum u_k^{-}$ aussi puis $\sum u_k$ converge.  

##### Cas complexe

Soit $k ∈ \mathbb{N}$,
$$
0 \le |\Re(u_k)|, |\Im(u_k)| \le |u_k|
$$

Donc $\sum |\Re(u_k)|, \sum |\Im(u_k)|$ convergent puis $\sum \Re(u_k), \sum \Im(u_k)$ convergent en revenant au cas réel.

enfin $\sum u_k$ converge.

#### Définition *Semi-convergence*

On dit que $\sum u_k$ est semi convergente si $\sum u_k$ converge mais pas absolument:

#### Exemple
$$
\sum \frac{(-1)^{k}}{k+1}
$$

#### Remarque

Si $\sum u_k$ converge absolument alors 
$$
∀ σ ∈ S_{\mathbb{N}}, \sum u_{σ (k)} \text{converge absolument et}
$$

$$
\sum_{k=0}^{+\infty} u_{σ (k)} = \sum _{k=0}^{+\infty} u_k
$$

MAIS SI $\sum u_k$ est SEMI CONVERGENT alors:
$$
∀ l ∈ \overline{\mathbb{R}}, ∃ σ ∈ S_{\mathbb{N}} / \sum_{k=0}^{+\infty} u_{σ (k)} = l !!!!!!!!!
$$

### Le critère des séries alternés

#### Théorème

On suppose que $(a_k)$ est décroissante et converge vers 0

- La série $\sum (-1)^{k} a_k$ converge
- Pour tout $n ∈ \mathbb{N} \cup {-1}, R_n$ est du signe de $(-1)^{n+1}$
- Pour tout $n ∈ \mathbb{N} \cup {-1}, |R_n| \le a_{n+1}$

En particulier, $\sum_{k=0}^{+\infty} (-1)^{k} a_k \le a_0$

#### Preuve

Soit
$$
S_n = \sum_{k=0}^{n} (-1)^{k} a_k
$$

Pour montrer que $(S_n)$ converge, il suffit de montrer que $(S_{2n})$ et $(S_{2n+1})$ convergent vers la même limite.

Il suffit de montrer que $(S_{2n})$ et $(S_{2n+1})$ sont adjacentes.

$$
S_{2(n+1)} - S_{2n} = -a_{2n+1} + a_{2n+2} \le 2
$$

car $(a_n)$ est décroissante.

$$
S_{2(n+1) + 1} - S_{2n+1} =  -a_{2n+3} + a_{2n+2} \ge 0
$$
car $(a_n)$ est décroissante.

Et $(S_{2n+1} - S_{2n} \to 0$ 

Les suites sont adjacentes.

Et $(S_n)$ converge.

- On note $S = \sum_{k=0}^{+\infty} (-1)^{k}$

donc $∀ n ∈ \mathbb{N}$,
$$
S_{2n+1} \le S \le S_{2n}
$$
- Donc $0 \ge S - S_{2n} = R_{2n} \ge S_{2n+1} - S_{2n} = -a_{2n+1}$
Et $R_{2n} \ge -a_{2n+1}$
- $0 \le S - S_{2n+1} = R_{2n+1} \le S_{2n+2} - S_{2n+1} = a_{2n+2}$

Ainsi $R_n$ est du signe de $(-1)^{n+1}$ et que $|R_n| \le a_n$

#### Exemple: "Le critère des séries de Riemann alternés"

Soit $α ∈ \mathbb{R}$

$$
\sum \frac{(-1)^{k}}{k^{α }} \text{ converge si et seulement si } α > 0
$$

- Si $α \le 0$ elle ne converge pas car $(-1)^{k}\times k^{- α  }$ ne converge pas vers 0 
- Si $α > 1$ elle converge car elle converge absolument.
- Si $α ∈ ]0,1]$ alors:
$$
\left(\frac{1}{k^{α }}\right)
$$
converge et est décroissant, donc par le critère des séries alternés, elle converge.

#### Remarque

Comment étudier la nature de la série:
$$
\sum u_k
$$

1. Si $u_k \to 0$
2. si $u_k > 0$ On effectue, une équivalence, un $\circ $  ou un $\bigcirc$, ou une inégalité pour se ramener a une série de référence.
3. si $u_k$ change de signe, on
    1. On étudie la convergence absolue
    2. critère des séries alternés
    3. On effectue un DL du terme général
    4. En dernier recours: Une transformation d'Abel


### Etude d'exemples

#### Exemple
$$
S = \sum \ln \left(1 + \frac{(-1)^{k}}{\sqrt{k}}\right)
$$

- $\ln (1 + (-1)^{k}/\sqrt{k}) \sim \frac{(-1)^{k}}{\sqrt{k}}$
- $\ln (1 + (-1)^{k}/\sqrt{k}) = \frac{(-1)^{k}}{\sqrt{k}} -\frac{1}{2k} + \bigcirc(\frac{1}{k^{3/2}})$
- $\sum \frac{(-1)^{k}}{\sqrt{k}}$ converge (Série de Riemann alternée)
- $\sum \frac{-1}{2k}$ diverge
- $\sum \frac{1}{k^{3/2}}$ converge (Sériee Riemann)
- Donc $S$ diverge.

#### Remarque

La série est équivalenet a une série convergente mais ne converge pas (car elle change de signe)

SI on ne veut pas calculer le $\bigcirc$ on peut montrer que:
$$
\ln (1 + \frac{(-1)^{k}}{\sqrt{k}}) - \frac{(-1)^{k}}{\sqrt{k}} \sim \frac{-1}{2k}
$$ 

qui elle est divergent et ne change pas de signe.

#### Exemple
Soit $z ∈ \mathbb{C}$

Montrons que:
$$
\sum \frac{z^{k}}{k!}
$$
converge et que
$$
\sum_{k=0}^{+\infty} \frac{z^{k}}{k!} = e^{z}
$$

Si $z = 0$, $\sum \cdots = 1 = e^{0}$

On suppose donc $z \neq 0$

On pose $u_k = |\frac{z^{k}}{k!}|>0$

$$
\lim_{n\to +\infty} \frac{u_{k+1}}{u_k} = \lim_{n\to+\infty} \frac{|z|}{n+1}
= 0
$$

Et $0 < 1$ donc par la règle de d'Alembert, $\sum u_k$ converge.

Donc $\sum \cdots$ converge absolument, elle converge donc. 

Calculons la valeur de $\sum_{k=0}^{+\infty} \frac{z^{k}}{k!}$

On utilise la formule d'intégration par parties généralisée:

Soit $n ∈ \mathbb{N}^{*}$ et $f,g ∈ C^{n}([a,b])$

On a:
$$
\int_{a}^{b} fg^{(n)}(t) dt = \sum_{k=0}^{n-1} (-1)^{k} [f^{(k)}(t) g^{(n-1-k)}(t)]_a^{b} + (-1)^{k} \int_{a}^{b} f^{n}g(t^{t}
$$

On montre cette formule par récurrence (en exercice)
On choisit
$$
f: t \mapsto e^{tz}, g : t \mapsto (t-1)^{n}
$$

a = 0, b = 1

On obtient:
$$
\int_{0}^{1} e^{tz} n! dt = \sum _{k=0}^{n-1} (-1)^{k} [z^{k}e^{tz} \frac{n!}{(n-(n-1-k))!} (t-1)^{k+1}] + (-1)^{n} \int_{0}^{1} z^{n} e^{tz} (t-1)^{n} dt
$$

$$
\frac{n!}{z} [e^{tz}]_0^{1} = \sum_{k=0}^{n-1} \frac{z^{k}}{(k+1)!}n! + (-z)^{n} \int_{0}^{1} e^{tz} (t-1)^{n}dt
$$

$$
e^{z} - 1 = \sum_{k=0}^{n-1} \frac{z^{k+1}}{(k+1)!} + \frac{(-z)^{n}}{n!} z \int_{0}^{1} e^{tz} (t-1)^{n} dt
$$

$$
e^{z} = \sum_{k=0}^{n} \frac{z^{n}}{n!} + \frac{(-z)^{n}}{n!} \times z \int _{0}^{1} e^{tz} (t-1)^{n} dt
$$

On pose $ε _n$:
$$
ε _n = z \times \frac{(-z)^{n}}{n!} \times \int_{0}^{1} e^{tz} (t-1)^{n}
$$ 

$$
0 \le |ε _n| \le \frac{|z|^{n+1}}{}\int_{0}^{1} |e^{tz}|dt \to 0
$$

donc quand $n \to +\infty$ on a:
$$
e^{z} = \lim_{n\to+\infty} \sum_{k=0}^{n} \frac{z^{k}}{k!}
$$

Enfin:
$$
e^{z} = \sum_{k=0}^{+\infty} \frac{z^{k}}{k!}
$$

#### Exemple
$$
\sum \frac{\cos k}{k}
$$

On pose pour $n ∈ \mathbb{N}, S_n = \sum_{k=1}^{n} \cos k / k$ 

On pose pour $j ∈ \mathbb{N}^{*}, T_j = \sum_{k=1}^{j} \cos k$

On observe que $∀ k ∈ \mathbb{N}^{*}, \cos k = T_k - T_k-1$ en posant $T_{0} = 0$

On a alors que $S_n = \sum_{k=0}^{n} \frac{T_k - T_{k-1}}{k}$

$$
S_n = \sum_{k=1}^{n} \frac{T_k}{k} - \sum_{k=1}^{n} \frac{T_{k-1}}{k}
$$

$$
S_n = \sum_{k=1}^{n} \frac{T_k}{k} - \sum_{k=0}^{n-1} \frac{T_{k}}{k+1}
$$
$$
S_n = \sum_{k=1}^{n} \frac{T_k}{k} - \sum_{k=0}^{n-1} \frac{T_{k}}{k+1}
$$
$$
S_n = \frac{T_n}{n} + \sum_{k=1}^{n-1} \frac{T_k}{k} - \frac{T_{k}}{k+1}
$$
$$
S_n = \frac{T_n}{n} + \sum_{k=1}^{n-1} \frac{T_k}{k(k+1)}
$$

Montrons que $(T_k)$ est bornée:

Pour demain:
1. Montrer que $(T_k)$ est bornée
2. Montrer que $(S_n)$ converge
3. Montrer que $\sum \frac{\cos k}{k}$ ne converge pas absolument
4. Demontrer le critere des séries alternées en faisant une transformation d'abel
5. On suppose que $\sum a_k$ converge, montrons que $\sum a_k / k$ converge.

## La formule de Stirling

#### Théorème
$$
n! \sim \sqrt{2 π n} \left(\frac{n}{e}\right)^{n}
$$

#### Preuve

##### Etape 1

On pose $w_n = \ln (n!) - \frac{1}{2} \ln (n)$

$w_{n+1} - w_n = (n + 0.5)(\ln (n) - \ln (n+1))$
$w_{n+1} - w_n = \bigcirc(\frac{1}{n^2})$

Donc $\sum \frac{1}{n^2} \to l$ et $\frac{1}{n^2} \ge 0$

Donc $\sum w_{n+1} - w_{n}$ converge

Par le critere des series telescopiques, $(w_n)$ converge vers $l$ sa limite donc:
$$
e^{w_n} \to e^{l}
$$  

Ainsi $∃ c > 0 / n! \sim c \sqrt{n} (\frac{n}{e})^{n}$

##### Etape 2 Calcul de c

Avec les intégrales de Wallis on obtient:
...

$ ∀n , (n+2)w_{n+2} = (n+1)w_n$

Par récurrence:
$$
∀ p, w_{2(p+1)} = \frac{2p+1}{2(p+1)} \times w_{2p} 
$$
$$
w_{2p} = \frac{(2p)!}{(2^pp!)^2} \times \frac{π }{2}
$$

## Produit de Cauchy

#### Définition *produit de convolution*

Soient $(u_n)$ et $(v_n)$ deux suites, on appelle produit de convolution de $u$ par $v$ la suite $u \star v$ définie par:
$$
u \star v = \sum_{k=0}^{n} u_k v_{n-k}
$$

#### Théorème "Produit de Cauchy de 2 suites absolument convergentes

On suppose que $\sum u_k$ et $\sum v_k$ convergent absolument 

Alors
$$
\sum (u \star v)_k
$$

Converge absolument, et:
$$
\sum_{k=0}^{+\infty} (u \star v)_k = \left(\sum_{k=0}^{+\infty} u_k\right) \times\left(\sum_{k=0}^{+\infty} v_k\right) 
$$

