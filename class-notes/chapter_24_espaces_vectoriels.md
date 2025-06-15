# Chapitre 24: Espaces Véctoriels

## Structure d'un espace véctoriel

### Loi de composition externe

#### Définition *Loi de composition externe*

Soit $E$ un ensemble,

On appelle loi de composition externe opérant de $\mathbb{K}$ sur $E$ toute application allant de $\mathbb{K} \times E$ dans $E$.
$$
(λ , \overrightarrow{x}) \mapsto λ .\overrightarrow{x}
$$

Une loi de composition externe est généralement notée avec un point.

Les éléments de $\mathbb{K}$ sont les scalaires, et ceux de $E$ sont les vecteurs.

Et sont surmontés temporairement d'une flèche.

#### Exemples

- $\mathbb{R}$ a une loi de composition externe a lui meme étant $\times$ sa  loi de composition interne.
- idem chez les complexes.
- On peut aussi prendre des $n-$uplets, $\mathbb{R} \times \mathbb{R}^{n} \to\mathbb{R}^{n}$ en associant $( λ , x_1, \cdots, x_n) \mapsto (λ x_1, \cdots λ x_n)$.

#### Définition *Espace véctoriel*

Soit $E$ un ensemble. On dit que $(E, +, \cdot)$ est un $\mathbb{K}-$espace véctoriel si $+$ est une loi de composition interne sur $E$, $\cdot$ une loi de composition externe opérant de $\mathbb{K}$ sur $E$ vérifiant:

1. $(E, +)$ soit un groupe abélien. 
2. $∀λ, μ  ∈\mathbb{K},  ∀\overrightarrow{x}, \overrightarrow{y}  ∈E$
    1. $λ ( \overrightarrow{x} + \overrightarrow{y}) = λ \overrightarrow{x} + λ \overrightarrow{y}$
    2. $( λ + μ ) . \overrightarrow{x} = λ \overrightarrow{x} + μ \overrightarrow{x}$
    3. $λ μ \overrightarrow{x} = λ ( μ \overrightarrow{x})$
    4. $1 \cdot \overrightarrow{x} = \overrightarrow{x}$


#### Exemples

- $(M_{n,p}(\mathbb{K}), +, \cdot)$
- $(\mathbb{K}^{n}, +, \cdot)$
- $(\mathbb{K}[X], +, \cdot)$
- $∀A,(\mathbb{K}^{A}, + , \cdot)$
    - En particulier $\mathbb{K}^{\mathbb{N}}$ est un $\mathbb{K}-$ev
- Plus généralement si $(E, +, \cdot)$ est un $\mathbb{K}-$ev, alors
- $∀A, (E^{A}, + \cdot)$ est un espace vectoriel.

### Remarques

Il faut faire la distinction entre les scalaires et les vecteurs.

1. Les scalaires étant des membres de $\mathbb{K}$ et les vecteurs membres de $E$.

2. En particulier, attention a ne pas confondre $0 ∈\mathbb{K}$ et $\overrightarrow{0_E}  ∈E$.

Si $E$ est un $\mathbb{C}-$espace vectoriel, alors $E$ peut s'interpréter comme un $\mathbb{R}$-espace véctoriel, en considérant les lois induites.

Réciproquement, si $E$, désigne un $\mathbb{R}-$-espace véctoriel, alors on ne peut pas (a priori) complexifier $E$. On peut en munissant $E \times E$ d'une structure de $\mathbb{C}$ (exo 1 du TD)

### Règles de calcul dans les éspaces vectoriels

#### Remarque

On peut sommer les vecteurs:
$$
\overrightarrow{x} + \overrightarrow{y}
$$

On peut multiplier par un scalaire
$$
λ \overrightarrow{ x}
$$

On peut le diviser par un scalaire non-nul
$$
\frac{1}{λ } \overrightarrow{x}
$$

#### Propriété

- $∀λ 1, \cdots, λ _n  ∈\mathbb{K},  ∀\overrightarrow{x}  ∈E$,
$$
(\sum_i λ _i) \cdot \overrightarrow{x} = \sum_i λ _i \overrightarrow{ x}$$
- $∀λ  ∈\mathbb{K},  ∀\overrightarrow{x_1}, \cdots \overrightarrow{x_n} ∈E$,
$$
λ \cdot (\sum_i \overrightarrow{x_i}) = \sum_i λ \overrightarrow{x_i}
$$
- $∀ λ  ∈\mathbb{K},  ∀\overrightarrow{x} ∈E,$
$$
λ \overrightarrow{x} = \overrightarrow{0_E} \iff (λ = 0 \lor \overrightarrow{x} = \overrightarrow{0_E})
$$
- $∀\overrightarrow{x}  ∈E$
$$
(-1) \cdot \overrightarrow{x} = - \overrightarrow{x}
$$

#### Preuve

"$\impliedby$":
$$
0 \cdot \overrightarrow{x} = (0+0) \cdot \overrightarrow{x}
$$
$$
0 \cdot \overrightarrow{x} = 0 \overrightarrow{x} + 0 \overrightarrow{x}
$$
$$
0 \cdot \overrightarrow{x} - 0 \cdot \overrightarrow{x} = 0 \cdot \overrightarrow{x}
$$
$$
\overrightarrow{0_E} = 0 \cdot \overrightarrow{x}
$$

(idem pour $\overrightarrow{0_E}$)


" $\implies$"

On suppose que $λ \overrightarrow{x} = \overrightarrow{0_E}$

si $λ = 0$ alors tant mieux,

sinon $λ \neq 0$ et

$$
\frac{1}{λ } \overrightarrow{x} = \frac{1}{λ } \cdot \overrightarrow{0_E}
$$

Donc
$$\left(λ \times \frac{1}{λ } \right)\cdot \overrightarrow{x} = \overrightarrow{0_E}
$$

puis

$$
1 \cdot\overrightarrow{x} = \overrightarrow{0_E}
$$

et

$$
\overrightarrow{x} = \overrightarrow{0_E}
$$

### COmbinaison linéaire d'une famille de vecteurs

#### Définition

Soit $(E, +, \cdot)$ un $\mathbb{K}-$espace véctoriel

Soit $n  ∈\mathbb{N}^{*}$ et soient $\overrightarrow{e_1}, \cdots, \overrightarrow{e_n}  ∈E$

On appelle combinaison linéaire des vecteurs $\overrightarrow{e_1}, \cdots, \overrightarrow{e_n}$

tout vecteur $\overrightarrow{x}$ de la forme:
$$
λ _i  ∈\mathbb{K}, \overrightarrow{x} = \sum_{i=1}^{n} λ_i \overrightarrow{e_i}
$$

#### Exemples

1. Dans le $\mathbb{R}-$espace véctoriel $\mathbb{C}$

On peut excrire tout complèxe comme combinaison linéaire de réels et de deux complexes, nottamment 1 et $i$.
$$
z = λ \cdot 1 + μ \cdot i 
$$

Mais aussi $1,j$

2. Dans le $\mathbb{K}-$espace véctoriel $\mathbb{K}[X]$

L'ensemble des combinaisons linéaires de $1, X, X^2$ est $\mathbb{K}_2[X]$.

L'ensemble des combinaisons linéaires de $L_0, \cdots, L_n$  est $\mathbb{K}_n[X]$

3. Dans le $\mathbb{K}-$espace véctoriel $M_n(\mathbb{K})$

L'ensemble des combinaisons linéaires de $E_{i,j} - E_{j,i}$

pour $1 \le i,j \le n$ est $\mathcal{A}_n(\mathbb{K})$

L'ensemble des combinaison linéaires de $E_{i,j}$ pour $1 \le i,j \le n$ est $M_n(\mathbb{K})$

4. Dans le $\mathbb{R}-$espace véctoriel $\mathbb{R}^{n}$

L'ensemble des combinaisons linéaires de $(1)$ et de $(n)$ sont les suites arithmétiques.

### Produits finis d'Espaces Véctoriels

#### Théorème

Soit $p  ∈\mathbb{N}^{*}$

Soient $(E_1, +, \cdot), \cdots, (E_p, +, \cdot)$ des $\mathbb{K}-$espaces véctoriels.

On pose $E = \prod _i E_i$

$$
\begin{cases}
+ : E \times E \to E  \\
 \left((\overrightarrow{x_1}, \cdots, \overrightarrow{x_p}), (\overrightarrow{y_1}, \cdots, \overrightarrow{y_p})\right) \mapsto (\overrightarrow{x_1} + \overrightarrow{y_1}, \cdots, \overrightarrow{x_p} + \overrightarrow{y_p})
\end{cases}
$$

et
$$
\begin{cases}
\cdot : \mathbb{K} \times E \to E \\
(λ , (\overrightarrow{x_1}, \cdots \overrightarrow{x_p})) \mapsto ( λ \overrightarrow{x_1}, \cdots λ \overrightarrow{x_p})
\end{cases}
$$

Alors $(E, +, \cdot)$ est un $\mathbb{K}-$espace véctoriel.

#### Preuve

A faire a la maison pour $p = 2$

## Sous-espace véctoriel

### Définition et caractérisation

#### Définition *Sous-espace véctoriel*

Soit $(E, +, \cdot)$ un $\mathbb{K}-$espace véctoriel.

Soit $F ⊂ E$

$F$ est un sous-espace de $E$ si:

- $\overrightarrow{0_E}  ∈F$
- $∀\overrightarrow{x}, \overrightarrow{y}, ∈ F, \overrightarrow{x}+\overrightarrow{y} ∈F$
- $∀ λ ∈\mathbb{K},  ∀\overrightarrow{x} ∈ F, λ \cdot \overrightarrow{x} ∈ F$

#### Remarque

Le premier point est superflu car il est compris dans le dernier en prenant $λ = 0$

#### Théorème "Caractérisation des sous-espaces véctoriels (SEV)"

Soient $E$ un $\mathbb{K}-$espace véctoriel et $F ⊂ E$. LASSE:

1. $F$ est un sous-espace véctoriel de $E$
2. $∀ λ ∈\mathbb{K},  ∀\overrightarrow{x}, \overrightarrow{y} ∈ F, λ \cdot \overrightarrow{x} + \overrightarrow{y}  ∈F$
3. $∀λ , μ  ∈\mathbb{K}, ∀\overrightarrow{x}, \overrightarrow{y} ∈ F, λ \cdot \overrightarrow{x} + μ \cdot \overrightarrow{y}  ∈F$

#### Preuve
Montons que toutes les assertions s'impliquent mutuellement

" $1 \implies 3$ ":
$$
λ \overrightarrow{x}  ∈F \text{ et } μ \overrightarrow{y} ∈F \text{ donc } λ \overrightarrow{x} + μ \overrightarrow{y} ∈F
$$

" $3 \implies 2$ ":
il suffit de choisir $μ = 1$

" $2 \implies 1$ ":
si $λ = 1$ on a:
$$
\overrightarrow{x} + \overrightarrow{y}  ∈F
$$
si $λ = -1$ et $\overrightarrow{x} = \overrightarrow{y}$
on a que $\overrightarrow{0_E}  ∈F$
si $\overrightarrow{y} = \overrightarrow{0_E}$
on a que $λ \overrightarrow{ x}  ∈F$

#### Remarque
 Si $F$ est un SEV de $E$ alors elle-l'est pour les lois induites.

#### Exemple

- $\{0\}, \mathbb{R}$ sont les SEV du $\mathbb{R}-$ev  $\mathbb{R}$
- $\{(0,0)\}, \mathbb{R}^2$ et toutes les droites passant par $(0,0)$
- $\{(0,0,0)\}, \mathbb{R}^3$ et toutes les droites et plans passant par $(0,0,0)$
- $\mathbb{R}[x], C^{n}(\mathbb{R})$ les fonctions paires et les fonctions impaires, sont des SEV du $\mathbb{R}-$ev $\mathbb{R}^{\mathbb{R}}$
- les suites airthmétiques, (pas les géométriques), suites géométriques de raison $a$ (pas les airthmétiques de raison $a$) (soit $a,b$ les sites de la forme $u_{n+2} = au_{n+1} + bu_n$ en sont)  les suites sont des SEV du $\mathbb{K}-$ev $\mathbb{K}^{\mathbb{N}}$
- l'esnsemble des soltions d'une équation différentielle linéaire homogène à coéfficients constants sur un intervalle $I$ de $\mathbb{K}$ est un SEV d $\mathbb{K}-$ev : $\mathcal{D}(I, \mathbb{K})$
- l'ensemble des solutions d'une équation différentielle linéaire d'ordre 2 homogène a coefficients constants sur un intervalle $I$ est un SEV du $\mathbb{K}-$ev : $\mathcal{D}^{2}(I, \mathbb{K})$
- $\mathbb{K}_n[X]$ est un SEV du $\mathbb{K}-$ev $\mathbb{K}[X]$
- $D_n(\mathbb{K}), T_n^{+}(\mathbb{K}), T_n^{-}(\mathbb{K}), S_n(\mathbb{K}), A_n(\mathbb{K})$ est un SEV du $\mathbb{K}-$ev $M_n(\mathbb{K})$

#### Théorème

Une intersection (quelconque) de SEV est un SEV

#### Preuve

On pose $F = \bigcap_{i  ∈I} F_i$
Montrons que $F$ est un SEV de $E$ par caractérisation.

$F \neq \varnothing$ car $\overrightarrow{0_E} ∈F$

Soient $λ  ∈\mathbb{K}, \overrightarrow{x}, \overrightarrow{y}  ∈F$

$\overrightarrow{x}, \overrightarrow{y} ∈F_i \implies λ \overrightarrow{x} + \overrightarrow{y}  ∈F_i \implies λ \overrightarrow{x} + \overrightarrow{y}  ∈F$

#### Remarque

En général une rénion n'est pas un SEV, amoins que l'un soit une partie de l'autre.

#### Remarque

Si $F$ est un SEV de $(E, +, \cdot)$ alors $(F, +)$ est un sous-groupe de $(E, +)$

#### Remarque

Soit $E$ un $\mathbb{K}-$ev et $r  ∈\mathbb{N}^{*}$ soient:
$$
E_1, \cdots, E_r
$$
des SEV de $E$

alors $E_1 ∪ E_2 ∪ \cdots ∪ E_r$ est un SEV si et seulement si:
$$
∃ i / \bigcup_{j=1}^{r} E_j ⊂ E_i
$$

#### Remarque pour Anas

Ceci est le seul résultat du chapitre ne fonctionnant que si $\mathbb{K}$ est infini.

### Sous-espaces véctoriels engendrées par une partie

#### Théorème

Soit $E$ un $\mathbb{K}-$ev et $A  ⊂E$

Il existe un unique sous-espace véctoriel $F$ de $E$ vérifiant:

- $A  ⊂F$
- Si $H$ est un sous-espace véctoriel de $E$ contenant $A$ alors $F  ⊂H$

On note $F = \text{Vect}(A)$ et on dit que $F$ est le SEV de $E$ engendré par $A$

#### Remarque

$\text{Vect}(A)$ se comprend comme le plus petit SEV de $E$ contenant $A$.

#### Exemples

- $\text{Vect}(\varnothing) = \{\overrightarrow{0_E}\}$
- $\text{Vect}(F) = F$ si $F$ est un SEV
- $\text{Vect}(\overrightarrow{x}) = \{ λ \cdot \overrightarrow{x} / λ  ∈\mathbb{K}\}$ pour $\overrightarrow{x}  ∈E$

#### Preuve

**Unicité**: Soient $F, F'$ deux SEV de $E$ vérifiant les conditions demandés

En particulier $F'$ est un SEV contenant $A$

Comme $F$ vérifie le second point on a : $F  ⊂F'$

Par symmétrie des roles on a l'autre inclusion et donc l'égalité

**Existence**:

On note $S$ l'ensemble des SEV de $E$ contenant $A$.

$S != \varnothing$ car $E  ∈S$.

On pose $F = \bigcap_{G  ∈S} G$

$F$ est un SEV de $E$ étant une intersection de SEVs

$∀ G  ∈S, A ⊂ G \implies A  ⊂F$

Soit $H  ∈S$, $F  ⊂H$.

#### Théorème

Soit $A  ⊂E$ ou $E$ est un $\mathbb{K}-$ev

$$
\text{Vect}(A) = \lbrace \sum λ _i \overrightarrow{x_i} /  ∀i, λ_i  ∈\mathbb{K}, \overrightarrow{x_i}  ∈A \rbrace
$$

#### Preuve

On note $B$ l'ensemble des combinaisons linéaires de $A$.

Comme $A ⊂\text{Vect}(A)$ alors $B ⊂\text{Vect}(A)$ car $\text{Vect}(A)$ est un SEV donc stable par combinaison linéaire.

(En exercice: montrer que $B$ est un SEV de $E$)

puis on observe que $A ⊂ B$ donc par construction $\text{Vect}(A) ⊂B$

Ainsi $B = \text{Vect}(A)$

#### Exemple

- $\text{Vect}(\overrightarrow{e_1}, \cdots \overrightarrow{e_n}) = \{ \sum λ_i \overrightarrow{e_i} / λ _i ∈ \mathbb{K}\}$

## Familles de vecteurs

### Famille génératrice

#### Définition Famille génératrice**

Soit $(E, +, \cdot)$ un $\mathbb{K}-$ev.

On dit qu'une famille $(\overrightarrow{e_i})_{i  ∈I}$
est génératrice si $\text{Vect}(\overrightarrow{e_i}, i ∈I) = E$

#### Remarque

$I$ peut être infini mais on ne réalise que des combinaisons linéaires finies.

#### Remarque

Une sur-famille (c.a.d. une famille a l'aquelle on a ajouté des vecteurs ) d'une famille génératrice le reste.

#### Propriété "Principe de Réduction des Familles génératrices"

Soit $(\overrightarrow{e_1}, \cdots, \overrightarrow{e_{n+1}})$ une famille génératrice de $E$

Si $\overrightarrow{e_{n+1}}  ∈\text{Vect}(\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$ alors

la famille $\overrightarrow{e_1}, \cdots, \overrightarrow{e_n}$ est génératrice de $E$.

#### Preuve

Soit $\overrightarrow{x}  ∈E$

$\overrightarrow{x}$ est une combinaison linéaire de $\overrightarrow{e_1}, \cdots \overrightarrow{e_n}, \overrightarrow{e_{n+1}}$

Or $\overrightarrow{e_{n+1}}$ est lui même combinaison linéaire des autres termes donc $\overrightarrow{x}$ est combinaison linéaire des autres en excluant $\overrightarrow{e_{n+1}}$

#### Exemples

Dans le $\mathbb{R}-$ev $\mathbb{C}$, $(1, i)$ et $(1, j)$ sont des familles génératrices.

Dans le $\mathbb{C}-$ev $\mathbb{C}$, $(1), (i), (1, i), (1, j)$ en sont.

Dans le $\mathbb{R}-$ev $\mathbb{R}^2$, $( (1,0), (0, 1))$

Dans le $\mathbb{K}-$ev $\mathbb{K}^{n}$ la famille:
$$
∀ 1 \le i \le n, \overrightarrow{e_i} = (0, \cdots, \overbrace{1}^{i\text{-eme position}}, \cdots, 0), (\overrightarrow{e_1}, \cdots, \overrightarrow{e_n}
$$

Dans le $\mathbb{K}-$ev des suites arithmétiques, $( (1), (n))$

Dans le $\mathbb{R}-$ev $\mathbb{R}_n[x]$ une famille génératrice est:
$$
(x \mapsto x^{k})_{0 \le k \le n}
$$


Dans le $\mathbb{R}-$ev $\mathbb{R}[x]$ une famille génératrice est:
$$
(x \mapsto x^{k})_{k  ∈\mathbb{N}}
$$


Dans le $\mathbb{K}-$ev $\mathbb{K}_n[X]$ une famille génératrice est:
$$
(X^{k})_{0 \le k \le n}
$$


Dans le $\mathbb{K}-$ev $\mathbb{K}[X]$ une famille génératrice est:
$$
(X^{k})_{k  ∈\mathbb{N}}
$$


Dans le $\mathbb{K}-$ev $\mathbb{K}_n[X]$ une famille génératrice est:
$$
(L_{k})_{0 \le k \le n}
$$

ou $L_k$ désignent les polynomes d'interpolation Lagrange associés a des élements $x_0, x_1, \cdots, x_n  ∈\mathbb{K}$ deux a deux distincs fixés une fois pour toutes.

Dans le $\mathbb{K}-$ev $M_{n,p}(\mathbb{K})$ la famille $(E_{i,j})_{1 \le i \le n, 1 \le j \le p}$

Dans le $\mathbb{K}-$ev $D_n(\mathbb{K})$ la famille $(E_{i,i})_{1 \le i \le n}$

Dans le $\mathbb{K}-$ev $T_n^{+}(\mathbb{K})$ la famille $(E_{i,j})_{1 \le i \le j\le n}$

Dans le $\mathbb{K}-$ev $S_n(\mathbb{K})$ la famille $(E_{i,j} + E_{j,i})_{1 \le i \le j\le n}$

Dans le $\mathbb{K}-$ev $A_n(\mathbb{K})$ la famille $(E_{i,j} - E_{j,i})_{1 \le i < j\le n}$

### Familles Libres

#### Définition *Famille Libre finie*

On dit que la famille (finie) de vecteurs $(\overrightarrow{e_1}, \cdots, \overrightarrow{e_n}$ est libre si,
$$
 ∀ λ _1, \cdots, λ _n  ∈\mathbb{K}, \sum λ _i \overrightarrow{e_i} = \overrightarrow{0_E} =\implies λ _1 = \cdots = λ _n = 0
$$

#### Définition *Famille Libre infinie*

On dit que la famille (infinie) de vecteurs est libre si, toutes ses-sous familles finies le sont.

Une famille non-libre est dite *liée*.

#### Exemple

Si $(\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$ est liée alors
$$
∃ λ _1, \cdots, λ _n  ∈\mathbb{K} / \sum λ _i \overrightarrow{e_i} = \overrightarrow{0_E}
 \text{ et } ∃ 1 \le i \le n / λ _i \neq 0
 $$

Donc $\overrightarrow{e_i} ∈ \text{Vect}(\overrightarrow{e_1}, \cdots, \hat{\overrightarrow{e_i}}, \cdots, \overrightarrow{e_n})$

#### Remarque

Une sous-famille d'une famille libre est libre.

#### Propriété "Principe d'extension des familles libres"

Soit $(\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$ une famille libre de vecteur de $E$.

Soit $\overrightarrow{e_{n+1}}  ∈E$

Si $\overrightarrow{e_{n+1}} ∉ \text{Vect}(\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$

Alors $(\overrightarrow{e_1}, \cdots, \overrightarrow{e_{n+1}})$ est libre.

#### Preuve

Soient $λ _1, \cdots, λ _{n+1}  ∈\mathbb{K} / \sum λ _i \overrightarrow{e_i} = \overrightarrow{0_E}$

Si $λ _{n+1} \neq 0$ alors $\overrightarrow{e_{n+1}} ∈\text{Vect}(\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$

Ce qui est absurde, donc $λ _{n+1} = 0$ et comme $(\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$ est libre on a: $∀i, λ _i = 0$

#### Exemples

- Une famille constituée d'un seul vecteur $\overrightarrow{x}$ est libre si et seulement si, $\overrightarrow{x} \neq \overrightarrow{0_E}$.
- Une famille de deux vecteurs $\overrightarrow{x}, \overrightarrow{y}$ est libre si et seulement si $\overrightarrow{x}, \overrightarrow{y}  ∉\text{Vect}(\overrightarrow{x}) \text{ ou exclusif } \text{Vect}(\overrightarrow{y})$ soit qu'ils soient colinéaires.
- Si $(\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$ est libre alors la famille est constituée de vecteurs 2-a-2 non-colinéaires  (réciproque fausse)
- Dans le $\mathbb{R}-$ev $\mathbb{C}$ $(1, i)$ est libre car un complexe est nul si et seulement si ses parties réelles et imaginaires sont nulles. 
- Dans le $\mathbb{R}-$ev $\mathbb{C}$ $(1, j)$ est libre car...
- Dans le $\mathbb{C}-$ev $\mathbb{C}$ $(1,i)$ n'est pas libre, mais $(1), (i), (j)$ le sont.
- Dans le $\mathbb{R}-$ev $\mathbb{R}^{\mathbb{R}}$ $(\cos, \sin)$ est libre. Soient $λ , μ  ∈\mathbb{R} /  ∀x  ∈\mathbb{R}, λ \cos x + μ \sin x = 0$, en évaluant en 0 on a $λ = 0$ et en $π / 2$ on a $μ = 0$

Élève modèle:
$$
∀x  ∈\mathbb{R}, λ \cos x + μ \sin x = 0
$$

or $λ \cos x$ est paire, et $μ \sin x$ impaire

Comme toute fonction s'ecrit comme la somme d'une fonction paire et impaire on a que $0 = 0_p + 0_i$

et on identifie $λ \cos x$ a  $0_p$ et $μ \sin x$  a $0_i$

Ainsi $λ = μ = 0$

Dans le $\mathbb{K}-$ev $\mathbb{K}_n[X], (X^{k})$ est une famille libre car $∀ λ _i  ∈\mathbb{K} \sum λ _i X^{i} = 0$ et deux polynomes sont egaux si et seulement si lesurs coéfficients sont égaux.

Dans le $\mathbb{R}-$ev $\mathbb{R}_n[x], (x \mapsto x^{k})$ est libre

**Méthode 1:**

le polynome $P = \sum λ _i X^{i} = 0$ donc il possède une infinité de racines, et il est donc le polynome nul.

Ainsi $λ _i = 0  ∀i$

**Méthode 2:**

Calculer les $n-$iemes dérivées puis évaluer en 0

**Méthode 3:**

$$
λ _0 + λ _1 x + \cdots + λ _n x^{n} + \circ (x^{n}) = \circ (x^{n})
$$

Donc par unicité des coéfficients d'un DL, on a que $λ _i = 0  ∀i$

Soient $x_0, \cdots, x_n  ∈\mathbb{K}$ 2-a-2 distincts on note $L_0, \cdots, L_n$ les polynomes d'interpolation de Lagrange associés a ces $x_i$

Alors $(L_k)$ est une famille libre du $\mathbb{K}-$ev $\mathbb{K}_n[X]$

Soit $0 \le i \le n$ en évaluant en $x_i$ on a $λ _i = 0$ Car $\tilde{L_i}(x_j) = δ _{i,j}$ 
