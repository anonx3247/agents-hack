# EM1: Notions sur le champ magnétique

## Le champ magnétique et ses sources

#### Définition *Champ*

La donée d'une grandeur en tout point de l'éspace.

#### Exemple

Pour le *champ de température* j'ai:

$$
 ∀M  ∈\mathcal{E}, T(M) = f(M)
$$

Ici c'est scalaire.

Pour le champ gravitationnel:

$$
\overrightarrow{g} = -g\overrightarrow{e_y}
$$

Ici il est vectoriel.

### Intéractions magnétiques

1. Pour des aimants de polarité $(1,-1)$ on a:

on peut décrire leur intéraction par la loi suivante:

$$
i = p_A \times p_B
$$

ou $p_I$ est la polarité de $I$ et si $i$ est positif il y a une répulsion, sinon une attraction.


2. Pour un aimant et un courant parcourant un fil, il y a aussi une intéraction.

3. Et il y en a entre deux courant parcourant deux fils.

### Le champ magnétique et ses sources

2. Courant $I \equiv$ source d'un champ magnétique $\overrightarrow{B}$.

Si le courant $I$ est orienté selon un axe $z$, $\overrightarrow{B}$ est dans le plan orthogonal a $z$ et de direction orthogonale a $I$ dans le sens trigonométrique pour un courant positif selon $z$.

On peut assimiler le champ engendré par le courant a un engendré par un aimant.


#### Définition *Champ magnétique*

Champ $\overrightarrow{B}$ véctoriel. (souvent noté $\mathbf{B}$)

Il est décrit par:

- direction
- sens
- intensité

Sources:

- aimants
- courants

## Propriétés du champ magnétique

### Carte de champ / Spectre magnétique

#### Exemples de spectres

##### Solénoide

Pour une ligne de champ $\mathcal{C}$, on a $∀M  ∈\mathcal{C}, \overrightarrow{B}(M) || \mathcal{C}$.

$\mathcal{C} = \{ \overrightarrow{dl} \land \overrightarrow{B} = \overrightarrow{0} \}$

Si on note $dS(M) / M ∈\mathcal{C}$ la distance entre $M$ et la surface du solénoide et $dS(\mathcal{C}) = \text{min }_{M  ∈\mathcal{C}} dS(M)$ alors

plus $d(\mathcal{C})$ est petit plus la courbe est petite.

Si on note $dC(M) / M ∈\mathcal{C}$ la distance entre $M$ et le centre du solénoide et $dC(\mathcal{C}) = \text{min }_{M  ∈\mathcal{C}} dC(M)$ alors

plus $d(\mathcal{C})$ est petit plus la courbe est grande avec $dC(\mathcal{C}) = 0 \implies l(\mathcal{C}) = +\infty$ ou $l(\mathcal{C})$ est la longeur de la courbe.

(Notations personelles)

##### Courant dans un fil

Les lignes de champ sont des cercles concentriques de centre le fil, et dans le plan normal au courant.

#### Interprétations de spectre

Propriétés des lignes de champ:

1. Elles sont toutes fermées (même si elles peuvent avoir une taille infinie.
2. Elles ne se croient jamais.
3. Les lignes orbitent autour des sources.


Propriétés du champ $\overrightarrow{B}$:

1. Le champ est tangeant aux lignes de champ et de même orientation.
2. On note $Δ(M)$ a densité relative des lignes de champ. Alors l'intensité est une fonction croissante de la densité. (notation personelle)


#### Application

1. $||\overrightarrow{B}(P)|| > ||\overrightarrow{Q}||$
2. Le champ est uniforme vers le bas, i.e il est égal en tout point $M$ de $S$.

On appelle $S$ une *zone de champ uniforme*.

### Intensité

#### Unité

L'unité du champ magnétique est le *Tesla* (T)

#### Mesure

mesuré avec un *tesla-mètre*

Un volt-mètre relié a une sonde a éffet Hall $u_H = k \times B_{ Δ }$

$$
\overrightarrow{F} = q\overrightarrow{v} \land \overrightarrow{B}
$$

#### Dépendance avec $I$ et la distance $r$

##### Distance $r$

L'intensité de $\overrightarrow{B}$ est d'autant plus faible que $r$ est grand.

$$
\overrightarrow{B} = \frac{μ _0 I}{2r} \overrightarrow{e_ θ}
$$

##### Courant $I$

Si la source est un courant.

Alors $I \nearrow \implies ||\overrightarrow{B}|| \nearrow$

Le comportement linéaire entre $I$ et $\overrightarrow{B}$ on a

$$
||\overrightarrow{B}|| \alpha I
$$

#### Ordres de grandeur

- Aimant de cuisine $B \sim 10^{-3} T$
- Champ magnétique terrestre $B \sim 10^{-4} / 10^{-5} T$
- Plus puissants aimants standards: $B \sim 1 T$
- Bobines supra-conductrices: $B \sim 10 T$
- Explosions qui reserrent les lignes de champ (non-permanent) $B \sim 100 T$ 

### Symmétries et invariances

#### Définition *Principe de Curie*

> "Les effets sont au moins aussi symmétriques que les causes"

#### Symmétries et invariances des sources

Soit un fil electrique droit infini

On prend un point situé autour du fil, de position $(r, θ, z)$

##### Invariances

- Il y a invariance de la distribution par $θ$ 
- Il y a invariance de la distribution par $z$ 
- Il n'y a pas invariance de la distribution par $r$

##### Symmétries

- Prenant un plan orthogonal au fil, le vecteur courant partant du plan de part et d'autre sont opposés, donc il y a une antisymmétrie par rapport au plan.

- Si l'on prend un plan comprenant le fil, alors c'est un plan de symmétrie.

#### Symmétries et invariances du champ $B$

##### Invariances de $B$

Les invariances de $B$ sont les mêmes que celles de la distribution.

Donc pour $B = B(r, θ, z)$ on a:

- $∀  θ,θ ', B(r,  θ,z) = B(r, θ ', z)$
- $∀z, z', B(r, θ, z) = B(r, θ, z')$


##### Symmétries de $B$

- $\overrightarrow{B}$ est un pseudo-vecteur (comme produit vectoriel de deux vrais vecteurs)

- $\overrightarrow{B} ∈$ plan d'antisymmétrie de la distribution
- $\overrightarrow{B} \perp$ plan de symmétrie de la distribution.

Ainsi $\overrightarrow{B} = B(r)\overrightarrow{e_ θ}$

#### Application

Spire de Courant:

Un courant $I$ en rotation circulaire autour de $O$ dans le plan $(Oxy)$ dans le sens trigonométrique avec $Oz$ vers nous.

Pour un point quelconque $M(r, θ, z)$, et un point de l'axe $N(0, θ, z)$

1. Montrer que $B(M)$ ne dépend pas de $θ$
2. Montrer que $\overrightarrow{B}(N) = B(N) \overrightarrow{e_z}$

1. Il y a une invariance de la distribution par $θ$ donc $B(M)$ ne dépend pas de $θ$
2. Pour tout plan contenant $Oz$ le fil est au même endroit donc il y a une antisymmétrie selon l'axe $Oz$. Ainsi tout ses plans contiennt $Oz$ donc  $\overrightarrow{B} ∈$ tous ses axes, ainsi il appartient a leur intersection, c.a.d. $Oz$ donc $\overrightarrow{B} || \overrightarrow{e_z}$

## Le dipole magnétique

Un dipole magnétique revient a une spire de courant.

Il est entierrement caractérisé par Le moment magnétique.

$$
\overrightarrow{m} = I \times S \times \overrightarrow{n}
$$

Ou $S$ est la surface de la spire

$\overrightarrow{n}$ est la normale au plan de la spire, et est donc orienté selon $I$, $I$ trigo $\implies$ la normale est vers vous, sinon, il va dans le sens opposé.

$[m] = I L^2$

$\overrightarrow{m}$ détermine $\overrightarrow{B}(M)$  dans tous l'espace.

L'orientation $N-S$ est telle que $S \to N$ soit dans le meme sens que $\overrightarrow{m}$.
