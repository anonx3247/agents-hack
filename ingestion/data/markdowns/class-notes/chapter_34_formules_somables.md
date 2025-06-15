# Chapitre 34: Formules Sommables

Dans ce chapitre on travaille dans un premier temps dans $(\overline{\mathbb{R}^{+}}, +, \times, \le )$

Ou
$$
\overline{\mathbb{R}^{+}} = \mathbb{R} ∪\{+ \infty\}
$$

$$
∀x ∈\overline{\mathbb{R}^{+}}, x \le + \infty
$$

$$
 ∀x  ∈\overline{\mathbb{R}^{+}}, x + (+\infty ) = + \infty
$$

$$
 ∀x ∈ \overline{\mathbb{R}^{+}} \backslash \{0\}, x \times (+ \infty) = + \infty
$$

$$
0 \times +\infty = 0
$$

#### Remarque

$$
0 \times \infty = 0
$$

N'est vrai que par convention et ne l'est pas pour une limite par exemple.

Dans ce chapitre $I$ désigne un ensemble non-vide.

## Familles sommables de réels positifs

### Definitions et Exemples

#### Définition *Famille sommable*

Soit $(a_i)  ∈\mathbb{R}_+^{I}$ une famille de réels positifs indexée par $I$.

On définit

$$
A = \{ \sum_{i  ∈J} a_i / J ⊂I, |J| < +\infty\}
$$

qui est une partie de $\mathbb{R}$ non-vide car $I \neq \varnothing$.

On dit que la famille $(a_i)_{i ∈I}$ est sommable si cet ensemble $A$ est majoré, et dans ce cas.

On note:

$$
\sum_{i  ∈I} a_i = \text{sup } A
$$

Sinon cet ensemble n'est pas majoré et on pose

$$
\sum_{i ∈I} a_i = +\infty = \text{sup }_{J ⊂ I} \left( \sum_{i  ∈J} a_i\right) 
$$

Et alors la famille n'est pas sommable.

#### Exemples

$$
K  ⊂I, \sum_{i  ∈K} a_i \le \sum_{i  ∈I} a_i
$$

En particulier si la famille est sommable pour $I$  alors elle l'est pour $K$.

#### Preuve

Si $(a_i)$ n'est pas sommable, l'égalité est banale car $\sum_{i  ∈I} a_i = + \infty$.

Sinon, on a $J  ⊂K$ on $J$ est fini, et alors

$$
\sum_{i  ∈J} a_i \le \sum_{i ∈I} a_i
$$


Vérifions que si $I$ est fini, alors $(a_i)$ est sommable et que

$$
\underbrace{\sum_{i  ∈I} a_i}_{\text{au sens de la borne sup des sommes des elements des sous ensembles finis de } I} = \underbrace{\sum_{i  ∈I} a_i}_{\text{Au sens d'une somme avec notation Σ}}
$$

La première est notée $S_1$ et la deuxième $S_2$.

Soit $K  ⊂I$

On a

$$
\sum_{i  ∈K} a_i \le S_2
$$

Donc $\{ \sum_{i  ∈J} a_i / J  ⊂I\}$ est majoré par $S_2$.

Ainsi $S_1 \le S_2$

Or $I ⊂I$ et est fini donc $S_2 \le \text{sup} \{\sum_{i ∈J} a_i / J vI\} = S_1$

Donc $S_1 = S_2$

On suppose a présent que $I = \mathbb{N}$

Donc on a $(a_i)  ∈\mathbb{R}_+^{\mathbb{N}}$

alors $(a_i)_{i  ∈\mathbb{N}}$ est sommable si et seulement si

$$
\sum_{k = 0}^{+\infty} a_i
$$

converge, et alors leur résultat sont les memes.

#### Preuve

On suppose que $(a_i)$ est sommable. Donc

Soit $n ∈\mathbb{N}$

$$
\sum_{i = 0}^{n} a_i \le \sum_{i  ∈ I} a_i
$$

Car $[0,n] ⊂\mathbb{N}$ et est fini.

La suite des sommes paritelles et majorée donc la série converge. En tant que série a termes positifs.

Donc par passage a la limite on obtient:

$$
\sum_{i = 0}^{+\infty} a_i \le \sum_{i  ∈I} a_i
$$

Sens indirect: On suppose maintenant que $\sum a_i$ converge.

Soit $J ⊂\mathbb{N}$ fini. Comme $J$ est fini il possède un majorant noté $n$.

Ainsi
$$
\sum_{i  ∈J} a_i \le \sum_{i= 0}^{n} a_i \le \sum_{i = 0}^{+\infty} a_i
$$

C'est bien majoré donc la borne supétieure existe et on a bien:

$$
\sum_{i  ∈I} a_i \le \sum_{i=0}^{+\infty} a_i
$$

Et il y a donc égalité.

#### Propriété

On suppose que $(a_i)$ est sommable, alors

$$
 ∀ ε > 0, ∃ J ⊂ I \text{ fini } /  ∀K \text{ fini } / J  ⊂K ⊂I
$$

$$
0 \le \sum_{i  ∈I} a_i - \sum_{i  ∈K} a_i \le ε
$$

(Si la famille est sommable alors le "reste" tend vers 0)

#### Preuve

Si $K  ⊂I$ et est fini alors

$$
\sum_{i  ∈K} a_i \le \sum_{i ∈I} a_i
$$

Donc leur différence est positive.

Soit $ε > 0$
D'après la caractérisation de la borne supérieure:
$$
∃ J  ⊂I / J \text{ fini et } \sum_{i  ∈J} a_i - ε \le \sum_{i  ∈I} a_i 
$$

Soit alors $K$ fini tel que $J ⊂ K  ⊂I$ alors:

$$
\sum_{i  ∈J} a_i \le \sum_{i  ∈K} a_i
$$

Donc

$$
\sum_{i  ∈I} a_i - ε \le \sum_{i  ∈K} a_i
$$

### Quelques Propriétés

#### Théorème "Croissance de la somme"

Soit $(a_i), (b_i)  ∈\mathbb{R}_+^{I}$ On suppose que $∀i   ∈I, a_i \le b_i$ alors

$$
\sum_{i  ∈I} a_i \le \sum_{i  ∈I} b_i
$$

Et si $(b_i)$ est sommable alors $(a_i)$ l'est aussi.

#### Preuve

Soit $J  ⊂I$ avec $J$ fini.

Donc

$$
\sum_{i  ∈J} a_i \le \sum_{i  ∈J} b_i
$$

En passant a la borne supérieure on a

$$
\sum_{i  ∈I} a_i \le \sum_{i ∈I} b_i
$$


#### Théorème "Invariance de la somme par permutation"

Soit $(a_i)$ une famille sommable de $\mathbb{R}_+^{I}$ et $σ  ∈S_I$

Alors

$$
\sum_{i  ∈I} a_i = \sum_{i ∈I} a_{ σ (i)}
$$

#### Preuve

On commence par prouver que

$$
\sum_{i  ∈I} a_{ σ (i)} \le \sum_{i  ∈I} a_i
$$

Si $(a_i)$ n'est pas sommable alors l'égalité est banale.

Sinon alors

Soit $J  ⊂I$ fini,

$$
\sum_{i ∈J} a_{ σ (i)} = \sum_{k  ∈σ (J)} a_k \le \sum_{i  ∈I} a_i
$$

Car $σ (J)$ est une partie finie de $I$.

Pour montrer l'autre inégalité on applique la premièrre inégalité a $a_{ σ (i)}$ et la permutation $σ ^{-1}$

On obtient:

$$
\sum_{i  ∈I} a_{ σ ( σ ^{-1}(i))} \le \sum_{i ∈I} a_i
$$

#### Théorème " $\mathbb{R}_+$-linéarité de la somme"

Soient $a,b  ∈\mathbb{R}_+^{I}$ et $λ , μ  ∈\mathbb{R}_+$

Alors
$$
\sum_{i  ∈I} λ a_i + μ b_i = λ \sum a_i + μ \sum b_i
$$

#### Preuve

On procède en deux temps

On commence par montrer que $\sum a_i + bi = \sum a+i + \sum b_i$

Puis que $\sum λ a_i = λ \sum a_i$.
$$
 ∀i  ∈I, a_i \le a_i + b_i
$$

Donc $(a_i + b_i)$ sommable $\implies$ $(a_i)$ sommable.

Donc par contraposée on a
$$
\sum_{i  ∈I} a_i + b_i = \sum_{i  ∈I} a_i + \sum_{i ∈I} b_i = +\infty
$$

Donc l'égalité est banale et $a, b$ jouent des roles symmétriques.

On suppose donc que $a, b$  sont sommables.

Soit $J  ⊂I$ fini.

$$
\sum_{i ∈J} a_i + b_i = \sum_{i ∈J} a_i + \sum_{i ∈ J} b_i
$$

En passant a la borne sup on a:

$$
\sum_{i ∈I} a_i + b_i \le \sum_{i ∈I} a_i + \sum_{i ∈ I} b_i
$$

Soit $ε > 0$

Alors $∃ J_1, J_2 ⊂ I$ finis, tels que:

$$
 ∀K_1, K_2, J_1 ⊂K_1 ⊂I, J_2 ⊂K_2 ⊂I / K_1, K_2 \text{ finis, on a:} 
$$

$$
0 \le \sum_{i  ∈I} a_i - \sum_{i  ∈K_1} a_i \le ε
$$

$$
0 \le \sum_{i  ∈I} b_i - \sum_{i  ∈K_2} b_i \le ε 
$$

On pose $K = J_1  ∪J_2$ de sorte que $K$ soit fini est vérifie:

$$
J_1 ⊂K  ⊂I, J_2 ⊂K ⊂I
$$

Et on a:

$$
\sum_{i  ∈I} a_i + \sum_{i  ∈I} b_i - 2 ε = (\sum_{i  ∈I} a_i - ε ) + ( \sum_{i  ∈I} b_i - ε ) \le \sum_{i  ∈K} a_i + \sum_{i ∈K} bi = \sum_{i  ∈K} a_i + b_i \le \sum_{i  ∈I} a_i + b_i
$$


Avec la linéarité des sommes finies.


### Le théorème de sommation par paquets dans le cas positif

#### Théorème "Le théorème de sommation par paquets dans le cas positif"

Soit $(a_i)  ∈\mathbb{R}^{I}_+$

On suppose que $I = \bigcup_{j ∈J} I_j$ avec
$$
 ∀i, k  ∈ J / i \neq k, I_i ∩ I_k = \varnothing
$$

Alors

$$
\sum_{i  ∈I} a_i = \sum_{j  ∈J} \left(\sum_{i  ∈I_j} a_i\right)
$$

Pour $j  ∈J$ on pose $σ_j = \sum_{i  ∈I_j} a_i  ∈\overline{\mathbb{R}_+}$

En particulier $(a_i)$ est sommable si et seulement si $( σ _j)_{j  ∈J}$ est sommable.

#### Exemple

Étudier la sommation de la famille:

$$
\left(\frac{1}{a^2+b^2}\right)_{a,b  ∈\mathbb{N}^{*}}
$$

$$
 ∀a,b  ∈\mathbb{N}^{*}, \frac{1}{a^2+b^2} \ge \frac{1}{(a+b)^2}
$$

$$
\mathbb{N}^{*} \times \mathbb{N}^{*} = \bigcup_{n \ge 2} \{ (a,b) ∈\mathbb{N}^{*} \times \mathbb{N}^{*} / a+b = n \}
$$

Cette union est disjointe.

Donc par sommation par paquets on a:

$$
\sum_{a,b ∈\mathbb{N}^{*}} \frac{1}{a^2+b^2} \ge \sum_{a,b  ∈\mathbb{N}^{*}} \frac{1}{(a+b)^2} = \sum_{n = 2}^{+\infty} \left(\sum_{(a,b)  ∈\mathbb{N}^{*} / a+b = n} \frac{1}{(a+b)^2}\right)
$$

$$
= \sum_{n = 2}^{+\infty} \frac{1}{n^2} \times n-1
$$

$$
\frac{n-1}{n^2} \sim \frac{1}{n}
$$

Donc elle diverge.

Et ainsi la famille n'est pas sommable.

#### Exemple

Étudier la sommabilité de la famille

$$
\left(\frac{1}{ab(a+b)}\right)_{a, b  ∈\mathbb{N}^{*}}
$$

$$
\sum_{a,b  ∈\mathbb{N}^{*}} \frac{1}{ab(a+b)} = \sum_{n = 2}^{+\infty} \left(\sum_{(a,b)  ∈\mathbb{N}^{*} \times \mathbb{N}^{*} / a+b = n} \frac{1}{ab(a+b)}\right)
$$

$$
= \sum_{n = 2}^{+\infty} \frac{1}{n} \times \left( \sum_{a=1}^{n-1} \frac{1}{a(n-a)}\right)
$$

$$
= \sum_{n = 2}^{+\infty} \frac{1}{n^2} \times \left(\sum_{a=1}^{n-1} \frac{1}{s} + \sum_{a=1}^{n-1} \frac{1}{n-a}\right)
$$

$$
\sum_{n=2}^{+\infty} \frac{1}{n^2} \times \left( H_{n-1} + \sum_{b=1}^{n-1} \frac{1}{b}\right)$$

$$
\sum_{n=2}^{+\infty} \frac{1}{n^2} \times \left( 2H_{n-1}\right)$$

$$
H_{n-1} \sim \ln n
$$

Donc

$$
\frac{H_n}{n^2} \sim \frac{\ln n}{n^2} = \circ \left(\frac{1}{n^{3/2}}\right)
$$

Or $3/2 > 1$ donc par Riemann, $\sum \frac{1}{n^{3/2}}$ converge.

Par composition sur les séries a termes positifs, $\sum \frac{H_{n-1}}{n^2}$ converge.

Donc la famille converge.

#### Preuve

Cas 1: SI la famille n'est pas sommable.

Soit $M ∈ \mathbb{R}_+$ On suppose que $∃ K  ⊂I$ fini tel que $M \le \sum_{i  ∈K} a_i$

On remarque que $K = K ∩ I$.
$$
K = K ∩ \left(\bigcup_{j  ∈J} I_j\right) = \bigcup_{j  ∈J} (K ∩ I_j)
$$

Soit $J_0 = \{j  ∈J / K ∩ I_j \neq \varnothing \}$

Donc

$$
K = \bigcup_{j  ∈J_0} (K ∩ I_j)
$$

Pour $j  ∈J_0$, $K ∩ I_j \neq \varnothing \iff ∃ x_j  ∈K ∩ I_j$ choisi au hasard.

On peut donc considérer l'application $φ$:

$$
φ : J_0 \to K
$$

$$
φ : j \mapsto x_j
$$

$φ$ est injective car les $x_j$ sont dans les $I_j$ disjoints donc
$j$ prend toujours une  valeur  unique.

$K$ est fini et $φ$ est injective donc $J_0$ est fini.

Donc

$$
M \le \sum_{i  ∈K} a_i = \sum_{j  ∈J_0} \left( \sum_{i  ∈K ∩ I_j} a_i\right)
$$

$$
\le \sum_{j  ∈J_0} \left(\sum_{i ∈I_j} a_i\right) \le \sum_{j  ∈J} \left( \sum_{i  ∈I_j} a_i\right)
$$

Donc $\sum_{i  ∈I} a_i = +\infty = \sum_{j  ∈J} \left( \sum_{i  ∈I_j} a_i \right)$


Cas 2: $(a_i)$ sommable.

Soit $ε > 0, ∃ K ⊂I$ fini tel que $\sum_{i  ∈I} a_i - ε \le \sum_{i  ∈K} a_i$

Par la même démarche que précédemment,

$$
\sum_{i  ∈K} a_i \le \sum_{j ∈J} \left(\sum_{i ∈I_j} a_i\right)
$$

On a donc une premièrre inégalité.

Donc
$$
\sum_{i  ∈K} a_i \le \sum_{j ∈J} \underbrace{\left(\sum_{i ∈I_j} a_i\right)}_{ σ _j}
$$

Soit $K = \{ j_1, \cdots, j_r\}$ une partie finie de $J$ de cardinal $r$.

Soient $I_1$ une partie finie de $I_{j_1} \cdots I_r$ une partie finie
de $I_{j_r}$.

$$
\sum_{k=1}^{r} \sum_{i  ∈I_{k}} a_i = \sum_{i  ∈\bigcup_{k=1}^{r} I_k} a_i \le \sum_{i  ∈I} a_i
$$

Donc
$$
\sum_{i  ∈I_1} a_i + \cdots + \sum_{i  ∈I_r} a_i \le \sum_{i ∈ I} a_i 
$$

En passant a la borne supérieure  en $I_1$ on obteint:

$$
\sum_{i  ∈I_{j_1}} a_i + \sum_{i  ∈I_2} a_i + \cdots \sum_{i  ∈I_r} a_i \le \sum_{i  ∈I} a_i
$$

En passant partout a la borne supérieure on a:

$$
\sum_{i  ∈I_{j_1}} a_i + \cdots + \sum_{i  ∈I_{j_r}} a_i \le \sum_{i ∈ I} a_i 
$$

$$
\sum_{j  ∈K} \left( \sum_{i  ∈I_j} a_i\right) \le \sum_{i ∈ I} a_i
$$

En passant a la borne supérieure sur $K$ on obtient l'autre inégalité.

## Familles sommables de réels et de complexes

Dans cette partie, $E$ désigneras $\mathbb{R}$ et $\mathbb{K}=\mathbb{R}$ ou bien $E$ désigneras $\mathbb{C}$ et dans ce cas, $\mathbb{K}=$ a $\mathbb{R}$ ou $\mathbb{C}$.

### Définitions et propriétés

#### Définition *Famille sommable*

Soit $(a_i)_{i  ∈I} ∈E^{I}$, on dit que la famille est sommable si:

$$
(|a_i|)_{i  ∈I}
$$

est sommable.

On note $l_1(I, E)$ ou $l_1(I)$ s'il n'y a pas d'ambiguité, l'ensemble des familles sommables a valeurs dans $E$, indexées par $I$.

#### Exemples

- Toute sous famille d'une famille sommable est sommable.
- Dans le cas ou $I = \mathbb{N}$ la famille est sommable si et seulement si la série $\sum a_i$ converge absolument.


#### Théorème

Soit $(a_i) ∈E^{I}$ dans le cas ou $E = \mathbb{R}$

Alors $(a_i)$ est sommable si et seulement si $(a_i)^{+}$ et $(a_i)^{-}$ sont sommables. Et dans ce cas:

$$
\sum_{i  ∈I} a_i = \sum_{i ∈I} a_i^{+} - \sum_{i  ∈I} a_i^{-}
$$

Dans le cas complexe, $(a_i)$ est sommable si et seulement si
$\Re(a_i)$ et $\Im(a_i)$ sont sommables  et alors

$$
\sum_{i  ∈I} a_i = \sum_{i  ∈I} \Re(a_i) + i \sum_{i  ∈I} \Im(a_i)
$$

#### Preuve

Si $E = \mathbb{R}$

$\implies$: $∀i  ∈I, 0 \le a_i^{+}, a_i^{-} \le |a_i|$

$\impliedby$: $∀i  ∈I, |a_i| = a_i^{+} + a_i^{-}$ donc sommable en tant que somme de 2 familles sommables.

Si $E = \mathbb{C}$ alors

$$
 ∀i  ∈I, 0 \le |\Re(a_i)|,|\Im(a_i)  \le |a_i| \le |\Re(a_i)| + |\Im(a_i)|
$$

Donc borné et ainsi , sommable.

#### Propriété

Soit $(a_i) ∈E^{I}$ une famille sommable.

$$
∀ ε > 0, ∃ J ⊂I \text{ finie } /  ∀J  ⊂K ⊂ I / K \text{ est finie on a:}
$$

$$
\left| \sum_{i  ∈I} a_i - \sum_{i  ∈K} a_i\right| \le ε 
$$

#### Preuve

Cas ou $E  =\mathbb{R}$, avec $ε > 0$.

Comme $a_i^{+}, a_i^{-}$ sont sommables.

$$
∃ J_+ ⊂ I \text{ finie } /  ∀J_+ ⊂ K_+ ⊂I \text{ avec } K_+ \text{ finie }, 0 \le \sum_{i  ∈I} a_i^{+} - \sum_{i  ∈K_+} a_i^{+} \le ε
$$
$$
∃ J_- ⊂ I \text{ finie } /  ∀J_- ⊂ K_- ⊂I \text{ avec } K_- \text{ finie }, 0 \le \sum_{i  ∈I} a_i^{-} - \sum_{i  ∈K_-} a_i^{-} \le ε
$$

On pose $J = J_+ ∪J_-$

Soit $J ⊂K  ⊂I$ tel que $K$ soit fini.

On a les 2 inégalités vérifées.

$$
\sum_{i ∈I} a_i - \sum_{i  ∈K} a_i = \left(\sum_{i  ∈I} a_i^{+} - \sum_{i  ∈I} a_i^{-}\right) - \left(\sum_{i  ∈K} a_i^{+} - \sum_{i ∈K} a_i^{-}\right)
$$

$$
= \left(\sum_{i  ∈I} a_i^{+} - \sum_{i  ∈K} a_i^{+}\right) - \left(\sum_{i  ∈I} a_i^{-} - \sum_{i  ∈K} a_i^{-}\right)
$$

Par les inégalités on a:

$$
- ε \le \sum_{i  ∈I} a_i - \sum_{i  ∈K} a_i \le ε
$$

En en passant a la valeure absolue on a l'inégalité souhaitée.

Si maintenant $E = \mathbb{C}$.

Soit $ε > 0$ avec les parties reelles et imaginaires sommables.

Par la même démarche on a

$$
\left| \sum_{i  ∈I} \Re(a_i) - \sum_{i  ∈K} \Re(a_i) \right| \le ε 
$$

$$
\left| \sum_{i  ∈I} \Im(a_i) - \sum_{i  ∈K} \Im(a_i) \right| \le ε 
$$

Ainsi $∃ J /  ∀K$ finies on a:
$$
\left| \sum_{i ∈I} a_i - \sum_{i  ∈K}  a_i\right| = \left| \sum_{i  ∈I} \Re(a_i) + i \sum_{i  ∈I} \Im(a_i) - \sum_{i  ∈K} \Re(a_i) - i \sum_{i  ∈K} \Im(a_i)\right|
$$

$$
\le \left| \sum_{i  ∈I} \Re(a_i) - \sum_{i ∈ K} \Re(a_i)\right| + \left| i\sum_{i  ∈I} \Im(a_i) - i\sum_{i  ∈K} \Im(a_i)\right| \le 2 ε
$$

### Propriétés des familles sommables

#### Théorème "Inégalité triangulaire"

Soit $(a_i)  ∈E^{I}$ une famille sommable:

$$
\left| \sum_{i  ∈I} a_i \right| \le \sum_{i  ∈I} |a_i|
$$

#### Preuve

On sait que
$∃ J ⊂I$ fini tel que $ ∀J  ⊂K ⊂I$ finies:

$$
\left| \sum_{i  ∈I} a-i - \sum_{i  ∈K} a_i\right| \le ε
$$

$$
= \left| \sum_{i  ∈I} a_i \right| = \left| \sum_{i  ∈I} a_i - \sum_{i  ∈K} a_i + \sum_{i  ∈K} a_i\right|
$$

$$
\le ε + \sum_{i  ∈K} |a_i| \le \sum_{i  ∈I} |a_i| + ε
$$

On fait tendre $ε$ vers 0  et on obteint le résultat voulu.

#### Théorème "Linéarité de la somme"

Soient $(a_i), (b_i) ∈ E^{I}$, deux familles sommables.

Soient $λ, μ  ∈\mathbb{K}$ alors $(λ a_i + μ b_i)_{i  ∈I}$ est sommable et alors:

$$
\sum_{i  ∈I} λ a_i + μ b_i = λ \sum_{i  ∈I} a_i + μ \sum_{i  ∈I} b_i
$$

#### Preuve

$$
 ∀i ∈I, 0 \le | λ a_i + μ b_i| \le | λ | |a_i| + | μ | |b_i| 
$$

Donc elle est sommable.

Pour pruver l'égalité, on procède en 2 temps:

1. $\sum_{i  ∈I} λ a_i = λ \sum_{i  ∈I} a_i$

2. $\sum_{i ∈I} a_i + b_i = \sum_{i  ∈I} a_i + \sum_{i  ∈I} b_i$

Pour $(1)$ on a:

$∃ K ∈I$ tel que:

$$
\left| \sum_{i  ∈I} λ a_i - \sum_{i  ∈K} λ a_i\right| \le ε
$$

et 
$$
\left| \sum_{i  ∈I} a_i - \sum_{i  ∈K} a_i\right| \le ε
$$

Donc

$$
\left| \sum_{i  ∈I} λ a_i - λ\sum_{i  ∈I} a_i\right|
$$

$$
= \left| \sum_{i  ∈I} λ a_i - \sum_{i  ∈K}  λ a_i - λ\sum_{i  ∈I} a_i + λ \sum_{i ∈K} a_i\right|
$$

$$
\le \left| \sum_{i  ∈I} λ a_i - \sum_{i ∈ K} λ a_i\right| + \left| \sum_{i  ∈K} λ a_i - \sum_{i  ∈I} λ a_i\right|
$$

$$
\le ε + | λ | ε = (1 + | λ |) ε
$$

Et si $ε \to 0$ on a l'inégalité:

$$
\left|\sum_{i  ∈I} λ a_i - λ \sum_{i∈ I} a_i \right| \le 0
$$

Pour $(2)$ on a:

Cas ou $E = \mathbb{R}$

$$
\sum_{i  ∈I} (a_i + b_i) = \sum_{i  ∈I} (a_i + b_i)^{+} - \sum_{i ∈ I} (a_i + b_i)^{-}
$$

Par $\mathbb{R}^{+}-$linéarité on a:

$$
(a_i + b_i)^{+} = a_i^{+} + b_i^{+} + \frac{|a_i+b_i|}{2} - \frac{|a_i| + |b_i|}{2}
$$
$$
(a_i + b_i)^{-} = a_i^{-} + b_i^{-} + \frac{|a_i+b_i|}{2} - \frac{|a_i| + |b_i|}{2}
$$

Vérifions cela pour:

1. $a_i, b_i \ge 0$
2. $a_i, b_i \le 0$
3. $a_i \ge 0, b_i \le 0$ et $a_i + b_i \ge 0$ 
4. $a_i \le 0, b_i \ge 0$ et $a_i + b_i \ge 0$

Or ses égalités sont composées de membres positifs donc on peut utiliser la $\mathbb{R}^{+}-$linéairté.

Et ils s'anullent (les parties $\frac{|a_i+b_i|}{2}, \frac{|a_i|+|b_i|}{2}$ de la partie positive et négative de la somme). 


$$
= \sum_{i  ∈I} a_i^{+} + \sum_{i  ∈I} b_i ^{+} - \sum_{ i  ∈I} a_i^{-} - \sum_{i  ∈I} b_i ^{-}
$$

$$
= \sum_{i  ∈I} a_i + \sum_{i  ∈I} b_i
$$

Cas ou $E = \mathbb{C}$

Alors

$$
\sum_{i  ∈I} a_i + b_i = \sum_{i  ∈I} \Re(a_i + b_i) + i \sum_{i  ∈I} \Im( a_i + b_i)
$$

$$
= \cdots
$$

#### Preuve

On peut aussi montrer ceci avec un raisonnement $ε$. Pour les cas complexes et réels.

Soit $ε > 0$
$∃ J ⊂I$ fini tel que:

$$
 \left|\sum_{i  ∈I} a_i - \sum_{i  ∈J} a_i\right| \le \varepsilon
$$

$$
 \left|\sum_{i  ∈I} b_i - \sum_{i  ∈J} b_i\right| \le \varepsilon
$$

$$
 \left|\sum_{i  ∈I} (a_i + b_i) - \sum_{i  ∈J} (a_i + b_i)\right| \le \varepsilon
$$

$$
 \left|\sum_{i  ∈I} \left(a_i + b_i\right) - \sum_{i  ∈I} a_i - \sum_{i  ∈I} b_i\right|
$$

$$
\le \left|\sum_{i  ∈I} \left(a_i + b_i\right) - \sum_{i  ∈J} \left(a_i + b_i\right)\right| + \left|\sum_{i  ∈I} a_i - \sum_{i \in J} a_i\right| + \left|\sum_{i \in I} b_i - \sum_{j \in J} b_i\right| + \left|\sum_{i \in J} \left(a_i+b_i\right) - \sum_{i \in J} a_i - \sum_{i \in J} b_i\right| $$

$$
\le ε + ε + ε + 0
$$

En faisant tendre $ε \to 0$ on a l'égalité voulue.


#### Théorème "Invariance par permutation"

Pour $σ  ∈S_I$ on a:

$$
\sum_{i ∈I} a_i = \sum_{i  ∈I} a _{ σ (i)}
$$

#### Preuve (Complexe)

Soient $(a_i)$ sommables  donc $(\Re(a_i)), (\Im(a_i))$

le sont aussi.

Donc $\Re(a_{ σ (i)})$ et $\Im(a_{ σ (i)})$ le sont aussi.

Donc $a_{ σ(i)}$ l'est aussi.

#### Théorème

On suppose $(a_i), (b_i) ∈E^{I}$ sommables.

Si $ ∀i  ∈I, a_i \le b_i$ alors $\sum_{i  ∈I} a_i \le \sum_{i  ∈I} b_i$

#### Preuve

$(b_i - a_i)  ∈l^{1}(I, \mathbb{R}^{+})$

Donc $\sum _{i  ∈I} (b_i - a_i) = \sum_{i  ∈I} b_i - \sum_{i  ∈I} a_i \ge 0$

#### Théorème

Soit $(a_i)  ∈E^{I}$ sommable

On suppose que $I = \bigcup_{j  ∈J} I_j$ disjoints.

Alors:

$$
\sum_{i  ∈I} a_i = \sum_{j  ∈J} \sum_{i  ∈I_j} a_i
$$

#### Preuve

Cas ou $E = \mathbb{R}$

$$
\sum_{i  ∈I} a_i^{+} = \sum_{j  ∈J} \sum_{i  ∈I_j} a_i^{+}
$$

$$
\sum_{i  ∈I} a_i^{-} = \sum_{j  ∈J} \sum_{i  ∈I_j} a_i^{-}
$$

Par différence on obtient l'égalité voulue
$$
\sum_{i  ∈I} \Re a_i = \sum_{j  ∈J} \sum_{i  ∈I_j} \Re a_i (*)
$$

$$
\sum_{i  ∈I} \Im a_i = \sum_{j  ∈J} \sum_{i  ∈I_j} \Im a_i (**)
$$

Par la somme $(*) + i(**)$ on a l'égalité souhaitée.

#### Remarque

Pour vérifier que $(a_i)$ est sommable, on applique le théorème de sommation par paquets dans le cas positif.

## Théorème de Fubini

### Le Théorème de Fubini positif

#### Théorème

Soient $I_1, I_2$ deux ensembles et $(a_{i,j}) ∈\mathbb{R}_+^{I_1 \times I_2}$

On a:
$$
\sum_{(i,j)  ∈I_1 \times I_2} a_{i,j} = \sum_{i  ∈I_1} \sum_{j  ∈I_2} a_{i,j} = \sum_{j  ∈I_2} \sum_{i  ∈I_1} a_{i,j}
$$

#### Preuve

On a: $I_1 \times I_2 = \bigcup_{i  ∈I_1} \{i\} \times I_2$

Par sommation par paquets positive, on a:

$$
\sum_{(i,j) ∈ I_1 \times I_2} a_{i,j} = \sum_{i  ∈I_1} \sum_{k  ∈\{i\} \times I_2} a_k = \sum_{i  ∈I_1} \sum_{j  ∈I_2} a_{i,j}
$$

### Le Théorème de Fubini

#### Théorème

Soient $I, J$ deux ensembles.

Soient $(a_{i,j})  ∈E^{I \times J}$

Alors, en supposant:

$$
\sum_{i  ∈I} \left( \sum_{j  ∈J} |a_{i,j}| \right) < +\infty
$$

on a:
$$
\sum_{i  ∈I} \sum_{j  ∈J} a_{i,j} = \sum_{j  ∈J} \sum_{i  ∈I} a_{i,j}
$$

#### Preuve

Soit $H  ⊂I \times J$ fini.

$∃ H_i ⊂I, H_j ⊂ J$ finis tels que $H ⊂H_i \times H_j$.

$$
\sum_{(i,j)  ∈H} |a_{i,j}| \le \sum_{(i,j)  ∈H_i \times H_j} |a_{i,j}|
$$

$$
\le \sum_{i  ∈H_i} \sum_{j  ∈H_j} |a_{i,j}| = \sum_{j  ∈H_j} \sum_{i  ∈H_i} |a_{i,j}|
$$

$$
\left\{ \sum_{\left(i,j\right) \in H} | a_{i,j} |  / H \subset I \times J, \text{et } H \text{ fini} \right\}
$$

est majoré donc la famille $(a_{i,j})$ est sommable.

### Remarque

$E$ et $\mathbb{R}_+$ ont des cadres différents.

- dans $\mathbb{R}_+$ on peut tout faire
- dans $E$ il y a des hypothèses a vérifier. Pour appliquer les théorèmes il faut vérifier la sommabilité, qui se vérifie par passage au module, et donc de retour au paradis.

### Exemples


#### Somme double avec $ζ$ 
Donnons sens et calculons

$$
\sum_{a \ge 2} \left(ζ (a) - 1\right) \times (-1)^{a}
$$

$$
ζ (s) = \sum_{k = 1}^{+\infty} \frac{1}{k^{s}} / s  ∈\mathbb{C}, \Re(s) > 1
$$

$$
= \sum_{a \ge 2} \sum_{k = 2}^{+\infty} \left(\frac{1}{k^{a}}\right) \times (-1)^{a}
$$

$$
= \sum_{k=2} ^{+\infty} \left( \sum_{a = 2} ^{+\infty} \left(\frac{-1}{k}\right)^{a}\right)
$$

$$
= \sum_{k = 2}^{+\infty} \frac{1}{1 + \frac{1}{k}} = \sum_{k = 2}^{+\infty} \frac{1}{k} - \frac{1}{k+1} = \frac{1}{2}
$$

Justification de l'utilisation du théorème de Fubini

Vérifions que
$$
\sum_{k = 2}^{+\infty} \sum_{a = 2}^{+\infty} \left|\frac{-1}{k}\right|^{a}
$$

est finie.

$$
= \sum_{k = 2}^{+\infty} \frac{1}{k(k-1)} = \sum_{k =2}^{+\infty} \frac{1}{k-1} - \frac{1}{k} = 1 < +\infty
$$

#### Arithmétique complexe

Soit $z  ∈\mathbb{C}$ tel que $|z| < 1$

Montrer que
$$
\sum_{a \ge 1} \frac{z^{a}}{a - z^{a}} = \sum_{n=1}^{+\infty} d(n)z^{n}
$$

ou $d(n) = |\{d  ∈\mathbb{N} / d | n\}|$

$$
\left|\frac{z^{a}}{1 - z^{a}} \right| \sim |z|^{a} \ge 0 
$$

Or $\sum |z|^{a}$ converge comme série géométrique, donc  la série converge absolument donc elle converge.

$0 \le |d(n) z^{n}| \le n |z|^{n} = \circ \left(\frac{1}{n^2}\right)$

Or $\sum \frac{1}{n^2}$ converge donc la série de droite converge.

$$
\sum_{a \ge 1} \frac{z^{a}}{1 - z^{a}} = \sum_{a \ge 1} \left( \sum_{b = 1}^{+\infty} z^{ab}\right)
$$

$$
= \sum_{a,b  ∈\mathbb{N}^{*} \times \mathbb{N}^{*}} z^{ab}
$$

On pose $n = ab  ∈\mathbb{N}^{*}$

$$
= \sum_{n = 1}^{+\infty} \sum_{a,b  ∈\mathbb{N}^{*} \times \mathbb{N}^{*} / ab = n} z^{ab}
$$

$$
= \sum_{n = 1}^{+\infty} z^{n} \sum_{a,b / ab = n} 1
$$

$$
= \sum_{n = 1}^{+\infty} z^{n} \times d(n)
$$

Justifications:

On applique le théorème de Fubini

$$
\sum_{a = 1}^{+\infty} \left( \sum_{b = 1}^{+\infty} |z^{ab}|\right) = \sum_{a = 1}^{+\infty} \sum_{b = 1}^{\infty} |z|^{a^{b}}
$$

$$
= \sum_{a = 1}^{+\infty} \frac{|z|^{a}}{1 - |z|^{a}} < +\infty
$$

car $\frac{|z|^{a}}{1 - |z|^{a}} \sim |z|^{a}$ et $(z^{ab})$ est sommable.

On applique le théorème de regroupement par paquets a $(z^{ab})$ en remarquant que

$$
\mathbb{N}^{*} \times \mathbb{N}^{*} = \bigcup_{n=1}^{+\infty} \left\{ (a,b)  ∈\mathbb{N}^{*} \times \mathbb{N}^{*} / ab = n \right\}
$$
