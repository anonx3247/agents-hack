# Chapitre 30: Intégration selon Riemann

## Uniforme continuité

Dans cette partie, $f$ est une fonction définie sur un intervalle $I$ de $\mathbb{R}$ contenant une infinité de points a valeurs dans $\mathbb{C}$ ou $\mathbb{R}$.

### Définition et Premières propriétés

#### Définition *uniformément continu*

On dit que $f$ est uniformément continue sur $I$ si et seulement si

$$
∀ ε > 0, ∃ δ _ ε > 0  /  ∀x,y  ∈I, |x-y| \le δ _ ε \implies |f(x) - f(y)| \le ε 
$$

#### Remarque

On a $f$ uniformément continue sur $I$ $\implies$ $f  ∈C^{0}(\mathbb{K})$.

#### Exemples

1. Si $f$ est constante
2. $x \mapsto x$ (avec $δ _ ε = ε$)
3. $[0,1] \to \mathbb{R} : x !\mapsto x^2$

On prend $ε$ et $(x,y)  ∈[0,1]^2$ fixés.

$$
|f(x) - f(y)| = |x^2 - y^2| = |x+y| |x-y| \le 2 |x+y|
$$

En prenant $δ _ ε = \frac{ε }{2}$ on a $|x-y| \le δ _ ε \implies |f(x) - f(y)| \le 2 δ _ ε = ε$

4. $x \mapsto x^2$ est un contrexemple.

On pose $n  ∈\mathbb{N}^{*}$

$$
\begin{cases}
x_n = n \\
y_n = n + \frac{1}{n}
\end{cases}
$$

$$
|y_n - x_n| = \frac{1}{n} \to 0
$$

$$
|f(y_n) - f(x_n)| = (n + \frac{1}{n})^2 - n^2
 = 2 + \frac{1}{n^2} \ge 2
 $$

Donc $f$ n'est pas uniformément continue sur $\mathbb{R}$.

#### Remarque

On peut noter que, pour montrer qu'une fonction n'est pas uniformément continue sur $I$, il suffit de trouver 2 suites de $I$ telles que
$$
\lim |x_n - y_n| = 0 \text{ et } \lim |f(x_n) - f(y_n)| > 0
$$

D'après le contrexemple, comme $x \mapsto x^2$ est continu sur $\mathbb{R}$ mais pas uniformément.

#### Propriété

Si $f$ est $k$-lipschitzienne sur $I$, alors $f$ est uniformément continue $I$.

#### Preuve

Soit $f$ une fonction $k$-lipschitzienne sur $I$.

$$
∃ k > 0 /  ∀(x,y)  ∈I^2, |f(x) - f(y)| \le k|x-y|
$$

Donc

$$
 ∀ε > 0 , ∃ δ _ ε = \frac{ε }{k} /  ∀(x,y) ∈I^2, |x-y| \le \frac{ε }{k} \implies |f(x) - f(y)| \le ε
$$

#### Remarque

La réciproque est fausse:
$$
x \mapsto \sqrt{x}
$$

Sa dérivée (sur $\mathbb{R}^{*}_+$) est non bornée donc elle n'est pas lipschitzienne.

Soient $ε > 0, x, y,  ∈\mathbb{R}^{*}_+$

$$
|f(x) - f(y)| = |\sqrt{x} - \sqrt{y}|
$$

Si $0 \le x,y \le ε ^2, |\sqrt{x} - \sqrt{y}| \le \sqrt{x} \text{ ou } \sqrt{y} \le ε$

Si $x > ε ^2$ ou $y > ε ^2$ on a alors

$$
|f(x) - f(y)| = \frac{|x-y|}{\sqrt{x} + \sqrt{y}} \text{ or } \sqrt{x} + \sqrt{y} > ε
$$

Donc $|f(x) - f(y)| \le \frac{|x-y|}{ε}$

D'ou il suffit de choisir $δ _ ε = ε ^2 > 0$

Ainsi dans les deux cas on a $|x-y| \le δ _ ε \implies |f(x) - f(y)| \le ε$.


En résumé: $f$ lipschitzienne $\implies f$ uniformément continue $\implies f$ continue

#### Théorème "Théorème de Heine"

Si $f$ est continue sur un segment $[a,b]$ alors $f$ est uniformément continue sur $[a,b]$

#### Preuve: non-éxigible

$f$ est continue sur $[a,b]$

On raisonne par l'absurde en supposant que $f$ n'est pas uniformément continue sur $[a,b]$.

Donc $∃ ε _0 > 0 /  ∀δ > 0, ∃ x,y  ∈I / |x-y| \le δ \text{ et } |f(x) - f(y)| > ε _0$

Soit $ε _0$ fixé, pour $δ = \frac{1}{2^{n}}$ il existe $x_n  ∈[a,b]$ et $y_n  ∈[a,b] / |x_n - y_n| \le \frac{1}{2^{n}}$ et $|f(x_n) - f(y_n)| > ε _0$\

Comme $(x_n)$ est bornée, par le théorème de Bolzano Wierstrass il existe $l  ∈[a,b]$ et $φ : \mathbb{N} \to \mathbb{N}$ strictement croissante telle que $(x_{φ (n)})$ soit convergente de limite $l$.

De même, comme $(y_n)$ est bornée il existe $l'$ et $ψ : \mathbb{N} \to \mathbb{N}$ strictement croissante telle que $(y_{ψ (n)})$ converge vers $l'$

Par propriétés des sous suites $(x_{φ ( ψ (n))})$ est aussi convergente de limite $l$

De plus, $∀ n  ∈\mathbb{N}, |x_{φ ( ψ (n))} - y_{ φ (ψ (n))}| \le \frac{1}{2^{φ ( ψ (n))}}$

Or comme $φ \circ ψ$ est strictement croissante par lemme vu pour les sous-suites, $φ ( ψ (n)) \ge n$ donc par minoration, $φ ( ψ (n)) \to_{n \to + \infty} + \infty$

Par passage a la limite, on a que $l = l'$.

Or on a aussi $|f(x_{φ ( ψ (n))}) - f(y_{ φ ( ψ (n))})| > ε _0$

Or comme $f$ est continue, par caractérisation séquentielle de la continuité puis par passage a la limite, on a $0 > ε _0 > 0$ ce qui est absurde.

Ainsi $f$ est uniformément continue sur $[a,b]$.

## Fonctions continues par morceaux sur un segment

### Subdivisions d'un segment

#### Définition *subdivision*

On appelle subdivision d'un segment $[a,b]$ toute suite finie $σ = (a_i)_{0 \le i \le n}$ telle que $a_0 = a < a_1 < \cdots < a_n = b$

Les $a_i$ sont appelés les points de la subdivision $σ$ et les intervalles $]a_{i-1}, a_i[$ pour $i  ∈[1,n]$ et appelées les intervalles de la subdivision  $σ$

#### Exemple

Soit $I = [0,2]$ et $σ = (0, \frac{1}{3}, \frac{1}{2}, 1, \frac{15}{8}, 2)$

$σ$ est une subdivision de $I$.

#### Définition *pas de subdivision*

Si $σ = (a_i)_{0 \le i \le n}$ est une subdivision de $[a,b]$ le réel $p( σ ) = \text{max}_{i  ∈[1,n]} (a_i - a_{i-1})$ s'appelle le pas de la subdivision $σ$.

#### Exemple

Dans l'Exemple précédent, $p( σ ) = a_4 - a_3 = \frac{7}{8}$

On utiliseras souvent la subdivision de $[a,b]$ suivante:

pour $n \ge 1$ on pose: $ ∀i  ∈[0, n]$,
$$
a_i = a + i \times \left(\frac{b-a}{n}\right)
$$

Le pas de toute sous-suite du type $i  ∈[k,m], 0 \le k < m \le n$  est le même.
$$
p ( σ ) = \frac{b-a}{n}
$$

On parle de subdivision a pas constant ou subdivision régulièrre

#### Définition *support de subdivision*

Soit $σ = (a_i)_{i  ∈[0,n]}$

L'ensemble $\text{supp}( σ ) = \{ a_i / i  ∈[0,n]\}$


#### Définition *subdivision plus fine*

Soient deux subdivisions $σ , σ '$

On dit que $σ '$ est une subdivision plus fine que $σ$ si
$$
\text{supp}( σ ) ⊂ \text{supp} ( σ '), \text{supp} ( σ ) \neq \text{supp} ( σ ')
$$

#### Exemple

Soient $σ = (0,\frac{1}{2}, 1)$ et $σ ' = (0, \frac{1}{4}, \frac{1}{2}, \frac{3}{4}, 1)$

$σ'$ est plus fine que $σ$.


#### Lemme

Si $S$ est un ensemble fini non-vide de points de $[a,b]$ (contenant $a$ et $b$)  , il existe une unique subdivision $σ$ de $[a,b]$ telle que $\text{supp}( σ ) = S$

#### Preuve

Comme $\mathbb{R}$ est totalement ordonné et $S$ est fini contenant $a,b$ en ordonnant les élements de $S$, on obtient une unique subdivision $σ$ de $[a,b]$.

#### Définition *réunion de subdivisions*

Soient $σ, σ '$ 2 subdivisions de $[a,b]$.

La subdivision $\text{supp} σ ∪\text{supp} σ '$ s'appelle la réunion des subdivisions et se note $σ ∪ σ '$.

#### Remarque

Comme $\text{supp}( σ )$ et $\text{supp} ( σ ')$ sont finis et contiennent $a,b$ leur réunion est bien finie et les contient aussi donc par le lemme $σ u σ '$ existe.

#### Exemple

$$
σ = (0, \frac{1}{2}, 1), σ ' = (0, \frac{1}{3}, \frac{2}{3}, 1)
$$

$$
σ  ∪σ ' = (0, \frac{1}{3}, \frac{1}{2}, \frac{2}{3}, 1)
$$

#### Propriété

Par construction, $σ  ∪σ '$ est une subdivision plus fine que $σ$ et $σ '$.

### Fonction en escalier sur un segment

#### Définition *Fonction escalier*

Une fonction $f : [a,b] \to \mathbb{R}$ est dite un escalier sur $[a,b]$ si il existe une subdivision $σ$ de $[a,b]$ telle que $f$ est constante a chaque intervalle $]a_{i-1}, a_i[$ pour $i  ∈[1,n]$.

Une telle subdivision est dite adaptée a $f$

On note $\mathcal{E}([a,b], \mathbb{R})$ l'ensemble des fonctions en escalier sur $[a,b]$

#### Remarque

1. Compte tenu de la définion d'une fonction en escalier, les valeurs prises par $f$ aux points d'une subdivision adaptée a $f$ n'ont pas d'importance.

2. Si $σ '$ est une subdivision plus fine de $[a,b]$ que $σ$ toutes les deux adaptées a $f$ on montre par récurrence sur le cardinal de $\text{supp}( σ' ) / \text{supp} ( σ )$ que $σ '$ est encore une subdivision adaptée a $f$

#### Propriétés

1. Si $f,g  ∈\mathcal{E}([a,b], \mathbb{R})$ et si $λ  ∈\mathbb{R}$, alors $λ f , |f|, f+g, f \times g  ∈\mathcal{E}([a,b], \mathbb{R})$

2. $\mathcal{E}([a,b], \mathbb{R})$ est un sev et un sous-anneau de $\mathbb{R}^{[a,b]}$

#### Preuve

1.

Soient $σ = (a_i)_{i  ∈[0,n]}$ et $σ ' = (b_i)_{i  ∈[0, n]}$

deux subdivisions adaptées respectivement a $f$ et $g$

Alors $∀ i  ∈[1,n]$ comme $f$ est constante sur $]a_{i-1}, a_i[$, $λ f, |f|$ sont en escalier.

De plus en posant $σ '' = σ  ∪σ '$ une subdivision plus fine et adaptée a la fois a $f$ et $g$. Donc si $σ '' = (c_i)$ comme $f$ et $g$ sont constantes sur les intervalles $]c_{i-1}, c_i[$ pour tout $i  ∈[1,p]$, $f+g, f \times g$ sont constantes sur chaqu'un de ceux-cis et sont donc en escalier.

2.

De plus les applications constantes $x \mapsto 0$ et $x \mapsto 1$ sont en escalier, et par les propriétés et les caractérisations de sous-anneau et de sev, $\mathcal{E}([a,b], \mathbb{R})$ est un sous-anneau et sev de $\mathbb{R}^{[a,b]}$

### Fonctions continues par morceaux

#### Définition *fonction continue par morceaux*

une fonction $f: [a,b] \to\mathbb{R}$ est dite continue par morceaux sur le segment $[a,b]$ s'il existe une subdivision $σ = (a_i)$ de $[a,b]$ vérifiant

1. $∀ i  ∈[1,n], f  ∈C^{0}(]a_{i-1}, a_i[, \mathbb{R})$

2. $∀ i  ∈[1,n], f(a_{i-1}^{+})$ et $f(a_i^{-})$ existent et sont finies.

Une telle subdivision est dite adaptée a $f$, on note $C^{0}_m([a,b], \mathbb{R})$ l'ensemble des fonctions continues par morceaux sur $[a,b]$ a valeurs dans $\mathbb{R}$.

#### Remarque

1. On peut étendre la définition d'une fonction continue par morceaux a un intervalle $I$ quelconque de $\mathbb{R}$ on diras que $f$ est continue par morceaux sur $I$ si elle l'est sur tout segment de $I$.

2. Si $f$ est continue par morceaux, et si $σ$ est une subdivision adaptée a $f$, les valeurs prises par $f$ aux points de $σ$ n'ont pas d'importance.

3. Si $σ'$ est plus fine que $σ$, $σ'$ est encore une subdivision adaptée a $f$

4. Par le théorème de prolongement par continuité, on a une définition équivalente des fonctions continues par morceaux:

$f$ est continue par morceaux sur $[a,b]$ si il existe une subdivision $σ = (a_i)$ vérifiant:

1. $∀i  ∈[1,n] f  ∈C^{0}(]a_{i-1}, a_i[, \mathbb{R})$

2. $∀ i  ∈[1,n] f$ se prolonge en une fonction continue sur $[a_{i-1}, a_i]$

#### Propriété

1. Soient $f,g  ∈C^{0}_m([a,b], \mathbb{R})$ et $λ  ∈\mathbb{R}$

Alors $|f|, λ f, f+g, f \times g$  sont aussi continues par morceaux sur $[a,b]$

#### Preuve

conférér  la démonstration pour les fonctions en escalier.

#### Propriété

Toute fonction continue par morceaux sur le segment $[a,b]$ est bornée sur ce segment.

#### Preuve

Soient $f  ∈C^{0}_m([a,b], \mathbb{R}), σ = (a_i)$ une subdivision adaptée a $f$.

Par la remarque, $f$ se prolonge en une application continjue sur tous les segments $[a_{i-1}, a_i]$ pour $i ∈[1,n]$ et par le théorème de continuité sur un segment, $f$ est bornée aur chaque intervalle.

En notant $M$ le maximum de toutes les bornes supérieures de $f$ sur ces segments, et $m$ le minimum de toutes les bornes inférieures de $f$ sur ses segments, on a $ ∀x  ∈[a,b], m \le f(x) \le M$.

### Approximation uniforme

#### Théorème

Soit $f  ∈C^{0}_m([a,b], \mathbb{R})$

Pour tout $ε > 0$, il existe $φ , ψ $ deux fonctions en escalier sur $[a,b]$ telles que :
$$
φ \le f \le ψ 
$$

et $0 \le ψ - φ \le ε$

#### Preuve

#### Lemme

Pour toute fonction continuepar morceaux sur $[a,b]$, il existe une fonction $g$ continue sur $[a,b]$ et une fonction $φ$ en escalier sur $[a,b]$ telles que $f = g \pm φ$

#### Preuve du lemme

Par récurrence forte sur $n  ∈\mathbb{N}$ de points de discontinuité de $f$

##### Initialisation

Si $n=0$, alors $f$ est continue sur $[a,b]$ donc on pose $g = f$ et $φ = Θ$

##### Hérédité

On suppose que toute fonction continue par morceaux sur $[a,b]$ et admettant au plus $n$ points de discontinuité s'écrit comme s'omme d'une fonction continue et s'une fonction escalier.

Soit $f  ∈C^{0}_m([a,b], \mathbb{R})$ avec $n+1$ points de discontinuité.

Soit $c$ l'un des points de discontinuité de $f$

###### 1er cas: $c  ∈]a,b[$

On pose $∀ x ∈[a,c[ , g(x) = f(x), g(c) = f(c^{-})$

$∀ x  ∈]a,b], g(x) = f(x) - f(c^{+}) + f(c^{-})$ 

Or par construction $\lim _{c^{-}} g = \lim _{c^{+}} g = g(c)$

Donc $g$ est bien continue qu point $c$

Comme $f= g$ sur $[a,c[$ le nombre de points de discontinuité de $f,g$ est le même sur $[a,c[$ et comme $g = f + cst$ sur $]c,b], g$ a au plus le même nombre de points de discontinuité que $f$ sur $]c,b]$

Donc $g$ admet au plus $n$ points de discontinuité.

Il existe $h  ∈C^{0}([a,b], \mathbb{R})$ et $φ_1, φ _2 ∈ \mathcal{E}([a,b], \mathbb{R})$ tels que $g = h + φ_1 [a,b] \to \mathbb{R}$

Or $f = g + φ _2$ avec
$$
φ _2 : \begin{cases}
x \mapsto 0 \text{ si } x  ∈[a,c[ \\
x \mapsto f(c) - f(c^{-}) \text{ si } x = c \\
x \mapsto f(c^{+}) - f(c^{-}) \text{ si } x  ∈]c, b]
\end{cases}
$$

Alors $f = h + φ _1 + φ _2$

Récurrence achevée.

Soit $f  ∈C^{0}_m([a,b], \mathbb{R})$, par le lemme, $∃ g  ∈C^{0}([a,b], \mathbb{R}), \tilde{φ }  ∈\mathcal{E}([a,b], \mathbb{R})$ tels que $f = g + \tilde{φ }$

Soit $ε > 0$ comme $g$ est continue sur $[a,b]$, par le théorème de Heine, $g$ est uniformément continue sur $[a,b]$ Donc il existe $δ _ ε > 0$ tel que:
$$
 ∀x,y  ∈[a,b], |x-y| \le δ _ ε \implies |g(x) - g(y)| \le ε
$$

Comme $\lim_{n \to +\infty} \frac{1}{n} = 0, ∃ n  ∈\mathbb{N}^{*} / \frac{1}{n} \le δ _ ε$

On pose alors $∀ i  ∈[0,n], a_i = a + i (b-a/n)$

---

Comme $g$ est continue sur $[a_{i-1}, a_i]$ pour $i  ∈[1,n]$

elle y est bornée et atteint ses bornes. Donc $∀i  ∈[1,n], ∃m_i, M_i  ∈\mathbb{R} /  m_i \le g(x) \le M_i$

De plus $∃ b_i , c_i ∈ [a_{i-1}, a_i] / m_i = g(b_i), M_i = g(c_i)$

---

Comme $g$ est continue sur $[a_{i-1}, a_i]$ pour $i  ∈[1,n]$

elle y est bornée et atteint ses bornes. Donc $∀i  ∈[1,n], ∃ m_i, M_i  ∈\mathbb{R} ∃ b_i, c_i  ∈[a_{i-1}, a_i] /$
$$
m_i = g(b_i) = \text{min}_{x  ∈[a_{i-1}, a_i]} g(x), M_i = g(c_i) = \text{max}_{x  ∈[a_{i-1}, a_i]} g(x)
$$

---

d'ou comme $|a b_i - c_i| \le |a_i - a_{i-1}| = \frac{1}{n} \le δ _ ε$

Alors $M_i - m_i \ge 0 \implies g(c_i) - g(b_i) \le ε$

On pose alors $∀x  ∈ ]a_{i-1}, a_i[, φ (x) = m_i, ψ (x) = M_i$

Puis $∀ i  ∈[0,n], φ (a_i) = ψ (a_i) = g(a_i)$

Par construction $φ, ψ$ sont en escalier sur $[a,b]$,

$$
φ \le g \le ψ, 0 \le ψ - φ \le ε
$$

Donc comme $f = g + \tilde{ φ}$, on a
$$
\overbrace{φ + \tilde{ φ }}^{\text{ en escalier}} \le f \le \overbrace{ψ + \tilde{ φ }}^{\text{en escalier}}
$$
$$
(ψ + \tilde{ φ }) - ( φ + \tilde{ φ }) = ψ - φ \le ε
$$





---

### Intégrale d'une fonction continue par morceaux sur un segment

#### Propriété

Soient $f, g$ dans $\mathcal{E}([a,b],\mathbb{R})$

1. Si $f \ge 0$ alors $I_{[a,b]}(f) \ge 0$
2. Si $f \ge g$ alors $I_{[a,b]}(f) \ge I_{[a,b]}(g)$

#### Preuve

1. Soit $σ = (a_i)_{0 \le i \le n}$ une subdivision adaptée a $f$

$$
 ∀i  ∈[0,n-1] ∃ λ _i  ∈\mathbb{R} /  ∀t  ∈]a_i,a_{i+1}[, f(t) = λ _i \ge 0 \text{ par hypothèse, donc } I_{[a,b]}(f) = \sum_{i=0}^{n-1} λ _i (a_{i+1} - a_i) \ge 0
$$

2. Si $f \ge g$ alors $f-g \ge 0$ donc on revient au point 1.

#### Propriété "Additivité par rapport a l'intervalle d'intégration"

Soit $f  ∈\mathcal{E}([a,b], \mathbb{R})$ et $c ∈]a,b[$

Alors
$$
I_{[a,b]}(f) = I_{[a,c]}(f) + I_{[c,b]}(f)
$$

#### Preuve

Soit $σ = (a_i)_{0 \le i \le n}$ une subdivision adaptée a $f$.

Quitte a considérer $σ  ∪\{c\}$ on pose qu'il existe $k  ∈[1,n-1] / a_k = c$ on a alors:
$σ _1 = (a_i)_{0 \le i \le k}$ une subdivision adaptée a $[a,c]$ et $σ _2 = (a_i)_{k \le i \le n}$ une subdivision adaptée a $[c,b]$ 

On a
$$
 ∀i  ∈[0,n-1] ∃ λ _i  ∈\mathbb{R} /  ∀t  ∈]a_i,a_{i+1}[, f(t) = λ _i \ge 0 \text{ par hypothèse, donc }
 $$

$$
I_{[a,b]}(f) = \sum_{i=0}^{n-1} λ _i (a_{i+1} - a_i)  = \sum_{i=0}^{k} (a_{i+1} - a_i) + \sum_{i=k}^{n} (a_{i+1} - a_i)
$$

#### Fonction continue par moceaux sur un segment

Soit $f  ∈C^{0}_m([a,b], \mathbb{R})$ $f$ est bornée sur $[a,b]$

Donc $∃ m, M  ∈\mathbb{R} /  ∀x  ∈[a,b], m \le f(x) \le M$

EN considérant $φ _0 : [a,b] \to \mathbb{R} / x \mapsto m$ et $ψ _0 : [a,b] \to \mathbb{R} / x \mapsto M$

$φ _0, ψ _0  ∈\mathcal{E}([a,b], \mathbb{R})$ et $φ _0 \le f \le ψ_0$

On pose:
$$
Φ = \{φ  ∈\mathcal{E}([a,b], \mathbb{R}) / φ \le f\}
$$
$$
Ψ = \{ψ  ∈\mathcal{E}([a,b], \mathbb{R}) / f \le ψ \}
$$

Ils sont non vides car $φ _0$ et $ψ _0$ leurs appartiennet respectivement.

Puis on pose
$$
I^{-} = \{ I_{[a,b]} (φ ) / φ  ∈Φ \}
$$
$$
I^{+} = \{ I_{[a,b]} (ψ ) / ψ   ∈Ψ  \}
$$

$I^{+}$ et $I^{-}$ sont non vides car $Φ , Ψ$  ne sont pas vides.

On a $∀φ  ∈Φ , φ \le f \le ψ _0$

Donc $I_{[a,b]}( φ )\le I_{[a,b]} (ψ _0) = M \times (b-a)$

Donc $I^{-}$ est une partie non vide et majorée par $M (b-a)$  de $\mathbb{R}$ donc par théorème, $α = \text{sup}(I^{-})$ existe et est fini.

De même $I^{+}$ admet une borne inferieure notée $β = \text{inf}(I^{+})$ finie.

#### Définition-Théorème

Soit $f  ∈C^{0}_m([a,b], \mathbb{R})$, avec les notations précédentes,

$α = β$ et on note alors:
$$
α = \int_a^{b} f(t) dt
$$

et on appelle l'intégrale de $f$ sur le segment $[a,b]$

#### Preuve

Soit $φ ∈Φ$ on a $∀ψ  ∈Ψ, φ \le f \le ψ$

Donc $I_{[a,b]} (φ) \le I_{[a,b]} (ψ )$, elle minore donc $I^{+}$

Par définition de la borne inférieure, on a que:
$$
I_{[a,b]} ( φ ) \le β 
$$

et cette inégalité est vraie pour tout $φ  ∈Φ$  Donc $β$ majore $I^{-}$ par définion de la borne supérieure:
$$
α \le β 
$$

Par le théorème d'approximation des fonctions continues par morceaux,

Soit $ε > 0$ 
$$
∃ φ _ ε  ∈Φ , ψ _ ε ∈Ψ , 0 \le ψ _ ε - φ _ε \le ε 
$$

Donc $ψ _ ε \le φ _ ε + ε$

D'ou:
$$
I_{[a,b]}(ψ _ ε ) \le I_{[a,b]} ( φ _ ε ) + (b-a) ε 
$$

Or $I_{[a,b]}  ∈I^{+}$ donc elle est plus grande que $β$

De même $I_{[a,b]} ( φ _ ε ) \le α$

Donc l'inégalité implique:

$$
β \le α + (b-a) ε 
$$

l'epsilon étant quelconque on peut le faire tendre vers 0 et on obtient:
$$
α \le β \le α \iff α = β
$$

#### Remarques

1. L'intégrale représente l'aire entre la courbe et l'axe des abscisses comptée positivement au dessus de l'axe et négativement en dessous.

2. Si $f  ∈\mathcal{E}([a,b], \mathbb{R})$ alors $f  ∈Φ ∩ Ψ$ et $I_{[a,b]}(f)$ corespond au $\text{max}(I^{-}) = \text{min}(I^{+})$ Donc

$$
I_{[a,b]}(f) = \int_a^{b} f(t)dt
$$

3. Compte tenu de la construction, de $\int_a^{b} f(t)dt$ on ne modifie pas sa valeur en changeant les valeurs prises par $f$ en un nombre fini de points.

#### Théorème

Soient $f,g  ∈C^{0}_m([a,b], \mathbb{R})$  et $λ  ∈\mathbb{R}$

Alors

$$
\int_a^{b} λ f(t) + g(t) dt = λ \int_a^{b}f(t)dt + \int_a^{b}g(t)dt
$$

#### Preuve

Montrons que l'intégrale d'une somme est une somme d'intégrales.

Soient $φ _1 , φ _2 ∈\mathcal{E}([a,b], \mathbb{R}) / φ _1 \le f, φ _2 \le g$ Alors $φ_1  φ _2 \le f + g$ et $φ _1 + φ _2  ∈\mathcal{E}([a,b], \mathbb{R})$

Donc
$$
\int_a^{b} φ _1(t) + φ _2(t) dt \le \int_a^{b} f(t) + g(t) dt
$$

par propriétés des intégrales de fonctions en éscalier:
$$
\int_a^{b} φ _1(t) + φ _2(t) dt = \int_a^{b} φ _1(t)dt + \int_a^{b} φ _2(t)dt
$$

En passant a la brone supérieure l'inégalité est vérifiée:
$$
\int_a^{b} f(t)dt + \int_a^{b} g(t)dt \le \int_a^{b} f(t) + g(t) dt
$$

Avec le même raisonnement sur la brone supérieure, on a égalité par double inégalité.

De manière analogue on montre que:
$$
\int_a^{b} λ f(t)dt = λ \int_a^{b} f(t)dt
$$

En trois cas:

1. $λ = 0$

2. $λ > 0$

3. $λ < 0$

#### Théorème

Soient $f,g  ∈C^{0}_m([a,b], \mathbb{R})$
(a noter que les inégalités suivantes n'ont de sens que si $a < b$) 
1. Si $f \ge 0$ alors $\int_a^{b} f(t)dt \ge 0$
2. SI $f \ge g$ alors $\int_a^{b} f(t)dt \ge \int_a^{b} g(t) dt$

#### Preuve

1. Si $f \ge 0$ alors la fonction nulle la minore, et son intégrale est nulle.

2. En repassant par le 1 avec la fonction $f-g$ puis on utilise la linéarité.

#### Théorème "Inégalité Triangulaire"

Soit $f  ∈C^{0}_m([a,b], \mathbb{R})$ avec $a < b$

Alors
$$
|\int_a^{b} f(t)dt| \le \int_a^{b}|f(t)|dt
$$

#### Preuve

Il est clair que si $f$ est continue par morceaux alors $|f|$ l'est aussi.

Et on a que $-|f| \le f \le |f|$ donc par le théorème précédent
$$
\int_a^{b} -|f(t)|dt \le \int_a^{b} f(t)dt \le \int_a^{b}|f(t)|dt
$$
et par linéarité
$$
-\int_a^{b} |f(t)|dt \le \int_a^{b} f(t)dt \le \int_a^{b}|f(t)|dt
$$
Or si $-a \le x \le a$ alors $|x| \le a$

Donc
$$
|\int_a^{b} f(t)dt| \le \int_a^{b}|f(t)|dt
$$

#### Théorème "Additivité par rapport a l'intervalle d'intégration"

Soit $f  ∈C^{0}_m([a,b], R\mathbb{R}, c  ∈[a,b]$

Alors
$$
\int_a^{b} f(t)dt = \int_a^{c} f(t)dt + \int_c^{b} f(t)dt
$$

#### Preuve

Soient $φ  ∈\mathcal{E}([a,b], \mathbb{R}) , φ \le f$

Alors
$$
\int_a^{b} φ (t)dt \le \int_a^{b} f(t)dt
$$
$$
\int_a^{c} φ (t)dt + \int_c^{b} φ (t)dt \le \int_a^{b} f(t)dt
$$

En passant a la borne supérieure on a:

$$
\int_a^{c} f (t)dt + \int_c^{b} f (t)dt \le \int_a^{b} f(t)dt
$$


Soient $ψ   ∈\mathcal{E}([a,b], \mathbb{R}) , f \le ψ$

Alors
$$
\int_a^{b} ψ  (t)dt \ge \int_a^{b} f(t)dt
$$
$$
\int_a^{c} ψ (t)dt + \int_c^{b} ψ  (t)dt \ge \int_a^{b} f(t)dt
$$

En passant a la borne supérieure on a:

$$
\int_a^{c} f (t)dt + \int_c^{b} f (t)dt \ge \int_a^{b} f(t)dt
$$


Enfin

$$
\int_a^{c} f (t)dt + \int_c^{b} f (t)dt = \int_a^{b} f(t)dt
$$

#### Convention

Si $a=b$ on pose:
$$
\int_a^{b} f(t)dt = 0
$$

et si $a > b$ on pose
$$
\int_a^{b}f(t)dt = - \int_b^{a}f(t)dt
$$

#### Théorème "Formule de Chasles"

Ceci est la même chose que le théorème précédent mais d'un autre nom, et a noter qu'elle reste vraie pour tout $a,b,c$ dans un intervalle $I$ de continuité de $f$.

$$
 ∀f  ∈C^{0}_m(I, \mathbb{R}),  ∀a,b,c  ∈I, \int_a^{c} f(t)dt = \int_a^{b}f(t)dt + \int_b^{c} f(t)dt
$$

#### Théorème

Soit $f  ∈C^{0}([a,b], \mathbb{R})$ et de signe constant sur $[a,b]$

Alors
$$
\int_a^{b} f(t)dt = 0 \iff f_{|[a,b]} = Θ 
$$

#### Preuve

$\impliedby$ trivial

$\implies$  Montrons le par contraposée

On prend $f \neq Θ$ et  montrons que son intégrale est non nulle.

Par linéarité de l'intégrale, on peut supposer $f \ge 0$
Comme elle est non nulle, il existe $x_0  ∈[a,b] / f(x_0) > 0$

Par continuité il existe un voisinage $[c,d]  ⊂[a,b] / c < x_0 < d$ tels que $ ∀x  ∈[c,d] , x > 0$


De plus comme elle est continue elle y est bornée et atteint ses bornes en particulier un minimum en $x_1, \text{min}_{[c,d]} f(x) = f(x_1)$

On a alors.

$$
\int_a^{b} f(t)dt = \int_a^{c} f(t) dt + \int_c^{d} f(t)dt + \int_d^{b} f(t)dt \ge \int_c^{d} f(t)dt \ge \int_c^{d} f(x_1)dt = (d-c)f(x_1) > 0$$

#### Propriété

Soit $f  ∈C^{0}([-a,a], \mathbb{R})$ avec $a>0$,

1. si $f$ est impaire alors $\int_{-a}^{a} f(t)dt = 0$

2. si $f$ est paire alors $\int_{-a}^{a} f(t)dt = 2 \int_0^{a} f(t)dt$

#### Preuve

On a
$$
\int_{-a}^{a}f(t)dt = \int_{-a}^{0} f(t)dt + \int_0^{a} f(t)dt
$$

Par changement de variable dans la premierre intégrale on a:

$$
\int_{-a}^{a}f(t)dt = \int_{0}^{a} f(-t)dt + \int_0^{a} f(t)dt
$$

Si $f$ est impaire alors $f(-t) = -f(t)$ et le résultat est nul, sinon si elle est paire $f(-t) = f(t)$ et le résultat est le double de l'intégrale de droite.

#### Propriété

Soit $f  ∈C^{0}(\mathbb{R})$ , $T-$périodique

Alors
$$
 ∀ x  ∈\mathbb{R}, \int_x^{x+T} f(t)dt = \int_0^{T} f(t)dt
$$

#### Preuve

$$
\int_x^{x+T} f(t)dt = \int_x^{0} f(t)dt + \int_0^{T} f(t)dt + \int_T^{x+T} f(t)dt
$$

Dans la derniere intégrale, on pose $u = t - T \iff t = u + T$

$$
\int_T^{x+T} f(t)dt = \int_0^{x} f(u+T)du = \int_0^{x}f(u)du
$$

d'ou:
$$
\int_x^{x+T} f(t)dt = \int_x^{0} f(t)dt + \int_0^{T} f(t)dt + \int_0^{x} f(t)dt = \int_0^{T} f(t)dt
$$

#### Théorème "Égalité de la moyenne généralisée"

Soient $f,g  ∈C^{0}([a,b], \mathbb{R})$ telles que $g$ soit de signe constant sur $[a,b]$.

Alors

$$
∃ c  ∈[a,b] / \int_a^{b} f(t)g(t)dt = f(c) \times \int_a^{b} g(t)dt
$$

#### Preuve

Par linéarité de l'intégrale, quitte a considérer $-g$ on peut la supposer positive.

Comme $f$ est continue le segment $[a,b]$ elle y est bornée et atteint ses bornes, notons les $f(α),f(β), α , β  ∈[a,b]$

Donc
$$
 ∀t  ∈[a,b], f( α ) \le f(t) \le f( β )
$$


Comme $g \ge 0$:

$$
 ∀t  ∈[a,b], f( α )g(t) \le f(t)g(t) \le f( β )g(t)
$$

par linéarité de l'intégrale et sa croissance on a:
$$
 f( α ) \int_a^{b} g(t) \le \int_a^{b} f(t)g(t) \le \int_a^{b} f( β )g(t)
$$

Si $\int_a^{b} g(t)dt = 0$ alors $\int_a^{b} f(t)g(t)dt = 0$ donc tout $c  ∈[a,b]$ convient.

Sinon comme $g \ge 0$, $\int_a^{b} g(t)dt > 0$

Donc

$$
f ( α ) \le \frac{1}{\int_a^{b} g(t)dt} \int_a^{b} f(t)g(t) dt \le f( β )
$$

Comme $f$ est continue sur $[a,b]$  par le TVI il existe $c  ∈[a,b]$ tel que
$$
f ( c ) = \frac{1}{\int_a^{b} g(t)dt} \int_a^{b} f(t)g(t) dt
$$

D'ou l'égalité.

#### Remarque

Si $g$ est la fonction constante égale a 1,
on obtient $∃ c  ∈[a,b] / \int_a^{b} f(t)dt = f(c) \times (b-a)$

c'est a dire que:
$$
∃ c  ∈[a,b] / \frac{1}{b-a} \int_a^{b} f(t)dt = f(c)
$$

#### Définition *valeur moyenne*

SI $f  ∈C^{0}([a,b], \mathbb{R}), (a < b)$
le réel $\frac{1}{b-a} \int_a^{b} f(t)dt$ s'appelle la valeur moyenne de $f$ sur $[a,b]$.

## Théorème fondamental de l'analyse

#### Théorème "Théorème Fondamental de l'Analyse"

Soit $I$ un intervalle de $\mathbb{R}$ non vide et non réduit a un point.

1. Toute fonction continue sur $I$ admet des primitives qui sont égales a une constante additive près.

2. Si $f  ∈C^{0}(I, \mathbb{R})$ et si $a ∈I$

alors l'application:
$$
F_a : x \mapsto \int_a^{x} f(t)dt
$$

est la primitive de $f$ s'anullant en $a$.

3. Si $f  ∈C^{0}(I, \mathbb{R})$, si $(a,b)  ∈I^2$ et si $F$ est une primitive de $f$ sur $I$ alors
$$
\int_a^{b} f(t)dt = [F(t)]_a^{b} = F(b) - F(a)
$$

et $∀x  ∈I, F'(x) = f(x)$

#### Preuve

Montrons (2).

Comme $f$ est continue sur $I$:
$$
 ∀x  ∈I, \int_a^{x} f(t)dt
$$

existe, donc $F_a$ est définie sur $I$.

Soit $x_0  ∈I$ montrons que $F_a$ est dérivable en $x_0$ et que $F'(x_0)f(x_0)$

C'est a dire, montrons que:
$$
\lim_{x \to x_0, x \neq x_0} \frac{F_a(x) - F_a(x_0)}{x - x_0} - f(x_0) = 0
$$

Soit $ε > 0$ alors $∀x ∈ I\backslash \{x_0\}$,

$$
\frac{F_a(x) - F_a(x_0)}{x - x_0} = \frac{1}{x-x_0} \left[ \int_a^{x} f(t)dt - \int_a^{x_0} f(t)dt \right] = \frac{1}{x - x_0} \left(\int_a^{x} f(t)dt + \int_{x_0}^{a} f(t)dt \right)
$$

Par la relation de Chasles
$$
= \frac{1}{x - x_0} \int_{x_0}^{x} f(t)dt
$$

Or $f(x_0) = \frac{1}{x - x_0} \int_{x_0}^{x} f(x_0) dt$

Donc
$$
A(x) = \frac{F_a(x) - F_a(x_0)}{x - x_0} - f(x_0)
$$

Et par linéarité de l'intégrale,

$$
A(x) = \frac{1}{x-x_0} \int_{x_0}^{x} (f(t) - f(x_0))dt
$$

$$
|A(x)| \le \frac{1}{|x-x_0|} \times | \int_{x_0}^{x} (f(t) - f(x_0))dt|
$$

Or $f$ est continue en $x_0$ donc $∃ α > 0 / ∀ x  ∈I, |x - x_0| \le α \implies |f(x) - f(x_0)| \le ε$


Étudions les deux cas:
1. Soit alors $x  ∈]x_0, x_0 + α [$

Alors $∀t  ∈[x_0, x]$

on a donc:$|f(t) - f(x_0)| \le ε$

par l'inégalité triangluaire on a:

$$
|A(x)| \le \frac{1}{x-x_0} \times \int_{x_0}^{x} |f(t) - f(x_0)|dt \le \frac{1}{x - x_0} \int_{x_0}^{x} ε dt = \frac{1}{x - x_0} \times ε (x - x_0) = ε
$$

2. Soit $x  ∈]x_0 - α, x_0[$

Alors $∀ t  ∈[x, x_0]$

on a donc:$|f(t) - f(x_0)| \le ε$

par l'inégalité triangluaire on a:

$$
|A(x)| \le \frac{1}{x_0-x} \times \int_{x}^{x_0} |f(t) - f(x_0)|dt \le \frac{1}{x_0 - x} \int_{x}^{x_0} ε dt = \frac{1}{x_0 - x} \times ε (x_0 - x) = ε
$$

Donc $∀ ε > 0, ∃ α > 0,  ∀x  ∈I \backslash \{x_0\}$

$$
|x - x_0| \le α \implies |\frac{F_a(x) - F_a(x_0)}{x - x_0} - f(x_0)| \le ε
$$

la limite existe donc bien est est bien finie.

Ainsi on a bien $F_a$ dérivable pour tout $x_0$ de dérivée égale a $f(x_0)$

Donc $F_a$ est dérivable sur I et $F_a' = f$ et $F_a$ est bien une primitive de $f$ sur $I$.

De plus :
$$
F_a (a) = \int_a^{a} f(t)dt = 0
$$

Démontrons a présent (1).

D'après (2) $f$ admet au moins une primitive $F_a$ aur $I$ avec $a  ∈I$ si $f$ est continue sur $I$.

De plus si $c  ∈\mathbb{R}, F_a + c$ est dérivable sur $I$
$$
(F_a + c) ' = F_a' + c' = f + 0 = f
$$

Donc toutes les applications: $x \mapsto F_a(x) + c / c  ∈\mathbb{R}$
Sont des primitives de $f$.

Réciproquement, si $G$ est une primitive de $f$ sur $I$ alors $G$ est dérivable sur $I$ et
$$
G' = f = F_a' \iff (G - F_a) ' = 0
$$

Comme $I$ est un intervalle, $(G - F_a)$ est une constante.

Donc toutes les primitives de $f$ sont égales a une constante additive près.

Ainsi (1) est prouvé, et avec l'unicité de la primitive $F_a$ s'anullant en $a$ car toutes les autres ne s'anulleront pas en $a$ mais en la constante les différentiant de $F_a$.

Enfin montrons (3).

Si $F$ est une primitive de $f$   sur $I$ alors

$$
∃ c  ∈\mathbb{R} / F = F_a + c
$$

Donc
$$
\int_a^{b} f(t)dt = F_a(b) = F_a(b) - F_a(a) = F_a(b) + c - (F_a(a) + c)
$$

$$
= F(b) - F(a)
$$

#### Remarque

Dans le théorème comme $f$ est continue sur $I$ si $F$ est une primitive de $f$ sur $I$, $F' = f$ donc $F  ∈C^{1}(I, \mathbb{R})$

## Sommes de Riemann

#### Théorème

Soit $f  ∈C^{0}_m([a,b], \mathbb{R})$ avec $a <b$

alors
$$
\lim_{n \to +\infty} \frac{b-a}{n} \sum_{k=0}^{n-1} f\left(a + k\frac{b-a}{n}\right) = \int_a^{b} f(t)dt
$$

#### Note

Si $n  ∈\mathbb{N}^{*}, S_n(f) = \frac{b-a}{n} \sum_{k=0}^{n-1} f\left(a + k \frac{b-a}{n}\right)$ s'appelle une somme de Riemann associée a $f$ sur $[a,b]$.

#### Remarque

Ai $a = 0$ et $b = 1$ on obtient
$$
\lim_{n \to +\infty} \frac{1}{n} \sum_{k=0}^{n-1} f\left(\frac{k}{n}\right) = \int_0^{1} f(t)dt
$$

#### Exemple

Calculer
$$
\lim_{n \to +\infty} \sum_{k=0}^{n-1} \frac{1}{n+k}
$$

On a $∀ n \ge 1 \sum_{k=0}^{n-1} \frac{1}{n+k} = \sum_{k=0}^{n-1} \frac{1}{1 + \frac{k}{n}}$

Soit $f : x \mapsto \frac{1}{1+x}, x  ∈[0,1]$

On recconnait une somme de Riemann associée a $f$ sur $[0,1]$

Comme $f$ est continue sur $[0,1]$, par le théorème la limite est égale a:
$$
\int_0^{1} \frac{1}{1+x} dx = \ln(2)
$$

#### Preuve

Au programme seulement si $f$ est $K-$lipschitzienne:
$$
 ∀x,y  ∈[a,b], |f(x) - f(y)| \le K |x - y|
$$

Soit $n \ge 1$ et on pose
$$
B_n \frac{b-a}{n} \times \sum_{k=0}^{n-1} f\left(a + k \frac{b-a}{n}\right) - \int_a^{b} f(t)dt
$$

et $∀ k  ∈[0, n]$, $a_k = a + k \frac{b-a}{n}$

Donc
$$
B_n = \sum_{k=0}^{n-1} \frac{b-a}{n} f(a_k) - \sum_{k=0}^{n-1} \int_{a_k}^{a_{k+1}} f(t)dt
$$

Or $∀ k  ∈[0,n-1], a_{k+1} - a_k = \frac{b-a}{n}$

Donc $∀ k  ∈[0,n-1]$
$$
\frac{b-a}{n} f(a_k) = (a_{k+1} - a_k) f(a_k) = \int_{a_k}^{a_{k+1}} f(t)dt
$$

Donc

$$
B_n = \sum_{k=0}^{n-1} \int_{a_k}^{a_{k+1}} (f(a_k) - f(t))dt
$$

Par l'inégalité triangulaire:
$$
|B_n| \le \sum_{k=0}^{n-1} \int_{a_k}^{a_{k+1}} |f(a_k) - f(t)|dt
$$

Par lipschitziennité:

$$
|B_n| \le \sum_{k=0}^{n-1} \int_{a_k}^{a_{k+1}} K|a_k - t|dt
$$

or $t  ∈[a_k, a_{k+1}]$ donc $|a_k - t| = t - a_k$

$$
|B_n| \le \sum_{k=0}^{n-1} \int_{a_k}^{a_{k+1}} K(t - a_k)dt
$$

$$
|B_n| \le \sum_{k=0}^{n-1} K \left[ \frac{1}{2} (t - a_k)^2 \right]_{a_k}^{a_{k+1}}
$$
$$
|B_n| \le \frac{K}{2} \sum_{k=0}^{n-1} (a_{k+1} - a_k)^2
$$
$$
|B_n| \le \frac{K}{2} \sum_{k=0}^{n-1}\frac{(b-a)^2}{n^2} = \frac{(b-a)^2}{2n} \times K
$$

Ce qui tend vers 0 lorsque $n \to +\infty$ et par le théorème d'encadrement, $|B_n| \to 0$

Et l'égalité est démontrée.

#### Remarques

1. On a également si $f  ∈C^{0}_m([a,b], \mathbb{R})$

$$
\lim_{n \to +\infty} \frac{b-a}{n} \sum_{k=0}^{n} f\left(a + k\frac{b-a}{n}\right) = \int_a^{b} f(t)dt
$$

2. Si on suppose $f  ∈C^{1}([a,b], \mathbb{R})$ alors par l'inégalité des accroissements finis on a:
$$
∀x, y  ∈[a,b], |f(x) - f(y)| \le |x - y| \times \text{max}_{t  ∈[a,b]} f'(t)
$$

Et la démonstration du théorème précédent fournie alors une majoration de l'érreur commise en remplaçant l'intégrale par la somme de Riemann.

On a:$|\int_a^{b} f(t)dt - \frac{b-a}{n} \sum_{k=0}^{n-1} f(a + k\frac{b-a}{n})| \le \frac{(b-a)^2}{2n} \times \text{max}_{t ∈ [a,b]} |f'(t)|$

## Les formules de Taylor

#### Théorème "formule de Taylor avec reste intégral"

Soient $a,b  ∈\mathbb{R} / a < b, n  ∈\mathbb{N}$ et $f  ∈C^{n+1}([a,b], \mathbb{R})$

Alors
$$
f(b) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(b-a)^{k} + \frac{1}{n!} \int_a^{b} (b-x)^{n} f^{(n+1)}(x) dx
$$

#### Preuve

Par récurrence sur $n$

Si $n = 0$ par hypothèse $f  ∈C^{1}([a,b], \mathbb{R})$

Donc
$$
\int_a^{b} f'(x)dx = f(b) - f(a)
$$

D'ou:
$$
f(b) = f(a) + \int_a^{b} f'(x)dx
$$

$$
f(b) = \sum_{k=0}^{0} \frac{f^{(k)(a)}}{k!}(b-a)^{k} + \frac{1}{0!} \int_a^{b} (b-x)^{0} f^{(0+1)}(x)dx
$$

Donc l'égalité est vérifiée au rang 0.

On la suppose vraie a un rang $n$ donné, Soit $f  ∈C^{n+2}([a,b], \mathbb{R})$

Alors $f$ est de classe $C^{n+1}$ sur $[a,b]$ donc par hypothèse:
$$
f(b) = \sum_{k=0}^{n} \frac{f^{(k)(a)}}{k!}(b-a)^{k} + \frac{1}{n!} \int_a^{b} (b-x)^{n} f^{(n+1)}(x)dx
$$

On pose $u(x) = f^{(n+1)}(x)$ et $v(x) = \frac{-1}{n+1}(b-x)^{n+1}$

$u, v$ sont $C^{1}$ sur $[a,b]$

$$
u'(x) = f^{(n+1)}(x), v'(x) = (b-x)^{n}
$$

Par intégration par parties
$$
\int_a^{b} (b-x)^{n} f^{(n+2)}(x)dx = \left[ \frac{-1}{n+1} (b-x)^{n+1} f^{(n+1)}(x)\right]_a^{b} + \frac{1}{n+1} \int_a^{b} (b-x)^{n+1} f^{(n+2)}(x)dx
$$

$$
= \frac{1}{n+1}(b-a)^{n+1} f^{(n+1)}(a) + \frac{1}{n+1} \int_a^{b} (b-x)^{n+1} f^{(n+2)}(x)dx
$$

Donc

$$
f(b) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(b-a)^{k} + \frac{1}{(n+1)!}(b-a)^{n+1} f^{(n+1)}(a) + \frac{1}{(n+1)!} \int_a^{b} (b-x)^{n+1} f^{(n+2)}(x)dx
$$

D'ou:

$$
f(b) = \sum_{k=0}^{n+1} \frac{f^{(k)}(a)}{k!}(b-a)^{k} + \frac{1}{(n+1)!} \int_a^{b} (b-x)^{n+1} f^{(n+2)}(x)dx
$$
On a l'hérédité.

#### Théorème "Inégalité de Taylor-Lagrange"

Soient $a, b  ∈\mathbb{R} / a < b, n  ∈\mathbb{N}, f  ∈C^{n+2}([a,b], \mathbb{R})$

Alors $|f(b) - \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(b-a)^{k}| \le \frac{(b-a)^{n+1}}{(n+1)!} \times \text{max}_{t  ∈[a,b]} |f^{(n+1)}(t)|$

#### Preuve

On utilise la formule de Taylor avec reste intégral


$$
|f(b) - \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(b-a)^{k}| = |\frac{1}{n!} \int_a^{b} (b-x)^{n} f^{(n+1)}(x)dx|
$$

$$
\le \frac{1}{n!} \int_a^{b} (b-x)^{n} |f^{(n+1)}(x)|dx
$$

Or $|f^{(n+1)}(x)|$ est continue sur le segment $[a,b]$ donc y est bornée et atteint ses bornes et le max existe.

Par croissance de l'intégrale on a
$$
\le \frac{1}{n!} \text{max}_{t  ∈[a,b]} |f^{(n+1)}(t)| \times \left(\int_a^{b} (b-x)^{n}dx  = \frac{1}{n+1} (b-a)^{n+1}\right)
$$

D'ou l'égalité.

#### Corollaire

Soit $f  ∈C^{n+2}(I, \mathbb{R})$ avec $I$ intervalle de $\mathbb{R}$ non vide et non réduit a un point.

$∀a, b  ∈I$,

1.
$$
f(b) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(b-a)^{k} + \frac{1}{n!} \int_a^{b} (b-x)^{n} f^{(n+1)}(x)dx
$$

2.
$$
|f(b) - \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(b-a)^{k}| \le \frac{(b-a)^{n+1}}{(n+1)!} \times \text{max}_{t  ∈[a,b]} |f^{(n+1)}(t)|
$$

#### Exemples


1. Montrons que $∀x  ∈\mathbb{R}^{+}$,

$$
x - \frac{x^3}{6} \le \sin x \le x - \frac{x^3}{6} + \frac{x^{5}}{120}
$$

Soit $f : t \mapsto \sin t - t + \frac{t^3}{6}$, $f$ est $C^3$ sur $[0,x]$ pour tout $x \ge 0$

Donc en applicant la formule de Taylor avec reste intégral a $f$ sur $[0,x]$ a l'ordre 2 on a alors:

$$
f(x) = f(0) + xf'(0) + \frac{x^2}{2}f''(0) + \frac{1}{2!} \int_0^{x} x^2 f^{(3)}(t)dt
$$

$$
f'(t) = \cos t - 1 + \frac{t^2}{2}, f(0) = 0
$$
$$
f''(t) = - \sin t + t, f'(0) = 0
$$
$$
f^{(3)}(t) = - \cos t + 1, f''(0) = 
$$

Donc
$$
f(x) = \sin x - x + \frac{x^3}{6} = \frac{1}{2} \int_0^{x} t^2 (1 - \cos t) dt \ge 0
$$

Donc
$$
 ∀x \ge 0, \sin x \ge x - \frac{x^3}{6}
$$

On pose a présent $g : t \mapsto \sin x$

D'après l'inégalité de Taylor lagrange on a:

$g  ∈C^{5}([0,x], \mathbb{R})$ pour tout $x \ge 0$

$$
g(0) = 0, g'(x) = \cos x, g'(0) = 1
$$
$$
g''(x) = - \sin x, g''(0) = 0
$$
$$
g^{(3)}(x) = - \cos x, g^{(3)}(0) = -1
$$
$$
g^{(4)}(x) = \sin x, g^{(4)}(0) = 0
$$
$$
g^{(5)}(x) = \cos x
$$

D'après l'inégalité a l'ordre 4 a $g$ sur $[0,x]$ on a:

$$
|g(x) - g'(0) - xg'(0) - \frac{x^2}{2} g''(0) - \frac{x^3}{6} g^{(3)}(0) - \frac{x^{4}}{24} g^{(4)}(0) - \frac{x^{5}}{120}| \le \frac{x^{5}}{120} \times \text{max}_{t  ∈[0,x]} |g^{(5)}(t)|
$$

D'ou
$$
|\sin x - x + \frac{x^3}{6} | \le \frac{x^{5}}{120}
$$

Or d'après la premierre inégalité, le membre de gauche est positif donc on peut enlever la valeur absolue

D'ou

$$
\sin x \le x - \frac{x^3}{6} + \frac{x^{5}}{120}
$$

2. Montrons que $∀x  ∈\mathbb{R},$

$$
\cos (x) = \sum_{n=0}^{+ \infty} \frac{(-1)^{n} x^{2n}}{(2n)!}
$$

On pose $f(t) = \cos t$

$$
f  ∈C^{\infty} ([0,x], \mathbb{R}) \iff  ∀N  ∈\mathbb{N}, f  ∈C^{N+1}([0,x], \mathbb{R})
$$

On vérifie par récurrence que
$$
 ∀n  ∈\mathbb{N},  ∀t  ∈\mathbb{R}, f^{(n)}(t) = \cos \left(t + n \frac{π }{2}\right)
$$

Ainsi si $n = 2p$ on a
$$
f^{(n)}(0) = \cos (0 + p π ) = (-1)^{p}
$$
Sinon si $n = 2p + 1$ on a
$$
f^{(n)}(0) = \cos \left(0 + \frac{π }{2} + p π \right) = 0
$$

On applique la formule de Taylor avec reste intégral a l'ordre $2N$ sur $[0,x]$ a $f, ∀x  ∈\mathbb{R}^{*}$ 

On a donc
$$
f(x) = \sum_{n=0}^{2N} \frac{f^{(n)}(a)}{n!}x^{n} + \frac{1}{(2N)!} \int_0^{x} (x - t)^{2N} f^{(2N+1)}(t)dt
$$

En faisant un regroupement par blocs
$$
f(x) = \sum_{p=0}^{N} \frac{(-1)^{p}}{(2p)!}x^{2p} + \underbrace{\frac{1}{(2N)!} \int_0^{x} (x - t)^{2N} \times \cos \left(t + (2N+1)\frac{π }{2} \right) dt}_{R_N(x)}
$$

Si $x > 0$

En applicant Taylor-Lagrange on a
$$
|R_N(x)| \le \frac{x^{2N+1}}{(2N+1)!}
$$

Par la formule de stirling quand $N \to +\infty$ $|R_N| \to 0$ par croissance comparée ($x^{p} = o(p!)$)

On a la même conclusion si $x < 0$:

Si $x = 0$, $x^{2p} = 0$ si $p \ge 1$ Donc la somme deviens égale a 1 ce qui reste vrai.

Si $x \neq 0$ D'après ce qui précede la série $\sum \frac{(-1)^{n}}{(2n)!}x^{2n}$ converge

En passant a la limite on a l'égalité souhaitée.

#### Remarques

1. Taylor-Lagrange lorsqu'on prend $b = 0$ revient a l'inégalité des acroissements finis, elle en est donc une généralisation.

2. Lorsque l'on applique la formule de Taylor avec reste intégral, ou l'inégalité de Taylor lagrange, il faut préciser la fonction $f$, le segment $[a,b]$ et l'ordre $n$.

3. La formule de Taylor-Young sert a démontrer une propriété locale (i.e. au voisinage d'un point), en revanche Taylor-Lagrange et la formule de Taylor avec reste intégral permettent de démontrer des propriétés globales sur un intervalle.



