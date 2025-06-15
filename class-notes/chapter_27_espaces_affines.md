# Chapitre 27: Espaces Affines

Dans ce chapitre, $E$ désigne un $\mathbb{R}-$ev.

## Espaces affines

### Définition

#### Définition *Espace affine*

On dit qu'un ensemble non vide $\mathcal{E}$ est un espace affine,
s'il existe un EV $E$, s'il existe une application  $\tilde{+}$ allant de $\mathcal{E} \times E \to \mathcal{E}$, vérifiant:

1. $∀ M  ∈\mathcal{E}, M \tilde{+} \overrightarrow{0} = M$
2. $∀ M  ∈\mathcal{E}, ∀ \overrightarrow{u}, \overrightarrow{v}  ∈E,$
$$
M \tilde{+} (\overrightarrow{u} + \overrightarrow{v}) = (M \tilde{+} u) \tilde{+} v
$$
3. $∀M,N  ∈\mathcal{E}, ∃ ! \overrightarrow{u} ∈E / M = N \tilde{+} \overrightarrow{u}$

#### Remarques

- le vecteur $\overrightarrow{u}$ reliant le point 3 est noté
$$
\overrightarrow{u} = \overrightarrow{NM}
$$

- Les points 2, 3 impliquent le point 1 (exo)

- En réalité dire que $\mathcal{E}$ est un espace affine signifie qu'il existe un EV $E$ tel que il agit sur $\mathcal{E}$ de manière simplement transitive.

- On dit que $\mathcal{E}$ est un espace affine de **direction** $E$.

- Un EV est constitué de vecteurs, et un EA est constitué de points.

Dans un EA on peut:

- sommer deux vecteurs,
- sommer un point avec un vecteur,
- on ne peut pas sommer deux points

### Exemples

- Un EV est un espace affine de direction lui-même et dans ce cas, $\tilde{+} = +$
- Soit $E$ un EV, soit $x_0 ∈E$, soit $F$ un SEV de $E$, on pose $\mathcal{E} = x_0 + F$, $\mathcal{E}$ est un espace affine de direction $F$

et $\tilde{+} : (x_0 + f, f') \mapsto (x_0 + f+ f')$

- Soit $\mathcal{E}$ un EA de direction $E$, soit $P_0  ∈\mathcal{E}$, soit $F$ un SEV de $E$.

On pose $\mathcal{F} = P_0 \tilde{+} F$, qui est un EA de direction $F$.

et $\tilde{+}^{\text{bis}} : (P_0 \tilde{+} f, f') \mapsto P_0 \tilde{+} (f + f')$

### Dimension d'un Espace Affine

#### Définition *Dimension d'un EA*

Soit $\mathcal{E}$ un EA de direction $E$,
alors
$$
\text{dim}(\mathcal{E}) = \text{dim}(E)
$$

### Règles de calcul dans un Espace Affine

On considère dorénavant $\mathcal{E}$ un EA de direction $E$

#### Propriétés

- $∀ M,N ∈\mathcal{E}, \overrightarrow{MN} = \overrightarrow{0} \iff M = N$
- $∀M,N  ∈\mathcal{E}, \overrightarrow{MN} = - \overrightarrow{NM}$

#### Preuve

- $\implies M = M \tilde{+} \overrightarrow{0} = M \tilde{+} \overrightarrow{MN} = N$
- $\impliedby M = N \tilde{+} \overrightarrow{0} = M + \overrightarrow{MN}$ par unicité de $\overrightarrow{u}$ réalisant $M \tilde{+} \overrightarrow{u} = N$ alors $\overrightarrow{MN} = \overrightarrow{0}$


$$
M \tilde{+} (\overrightarrow{MN} + \overrightarrow{NM})
$$
$$
= M \tilde{+} \overrightarrow{MN} \tilde{+} \overrightarrow{NM}
$$
$$
= N \tilde{+} \overrightarrow{NM}
$$
$$
= M = M \tilde{+} \overrightarrow{0} \iff (\overrightarrow{MN} + \overrightarrow{NM}) = \overrightarrow{0} 
$$

#### Propriété "Relation de Chasles"

$∀A, B, C ∈\mathcal{E}, \overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{BC}$

#### Preuve

$A \tilde{+} \overrightarrow{AC} = C$

$A \tilde{+} (\overrightarrow{AB} + \overrightarrow{BC}) = C$

donc $\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{BC}$

### Repère affine

#### Définition *Repère affine*

On dit que $\mathcal{R} = (O, \mathcal{B})$ est un repère affine si $O  ∈\mathcal{E}$ et $\mathcal{B}$ est une base de $E$.

$O$ s'appelle l'origine du repère $\mathcal{R}$.

#### Définition *coordonnés d'un point*

Soit $\mathcal{R}(O, (\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$ un repère affine

$$
 ∀M  ∈\mathcal{E}, ∃ ! ( λ _1,\cdots, λ _n) ∈\mathbb{R}^{n} / \overrightarrow{OM} = \sum_{i=1}^{n} λ _i \overrightarrow{e_i}
$$

$λ _1, \cdots, λ _n$ sont les coordonnés de $M$.

#### Définition *affinement indépendents*

Soit $A_0, \cdots, A_n$ des points de $\mathcal{E}$,

ils sont affinement indépendents si $(\overrightarrow{A_0A_1}, \cdots, \overrightarrow{A_0A_n})$ est une famille libre de $E$.

#### Exercice
Vérifier que $A_0$ n'a pas été privilégié

#### Théorème

On suppose $\text{dim} E = n$ si $\mathcal{A_0}, \cdots, \mathcal{A_n}$ sont affinement indépendents alors:
$$
\mathcal{R} = (A_0, (\overrightarrow{A_0A_1}, \cdots, \overrightarrow{A_0, A_n}))
$$

Est un repère de $\mathcal{E}$.

## Sous-espaces Affines

### Définition

#### Définition *Sous-espace affine*

Soit $\mathcal{E}$ un EA de direction $E$,

Soit $\mathcal{F} ⊂ \mathcal{E}$ non vide.

$\mathcal{F}$ est un SEA de $\mathcal{E}$ si il existe $A  ∈\mathcal{E} / \mathcal{F} = \{\overrightarrow{AM} / M  ∈\mathcal{F}\}$

#### Théorème

Soit $\mathcal{E}$ un EA de direction $E$,

soit $\mathcal{F} ⊂\mathcal{E}$

$\mathcal{F}$ est un SEA de $\mathcal{E}$ si et seulement si,
$$
∃ A  ∈\mathcal{F} / ∃ F \text{ un SEV de } E / \mathcal{F} = A \tilde{+} F
$$

En particulier, un SEA est uniquement déterminé par la donnée d'un point et s'un SEV qui seras sa direction.

De plus

$$
 ∀B  ∈\mathcal{F}, \mathcal{F} = B \tilde{+} F
$$

#### Preuve

Admis (long, facile, inintéressant)

$\mathcal{F}$ est alors un EA de direction $F$.

### Reformulation dans les espaces vectoriels

#### Théorème

Soit $E$ un EV

Soit $\mathcal{F}$ une partie de $E$

$\mathcal{F}$ est un SEA de $E$ si et seulement si,

$∃ \overrightarrow{a}  ∈E, ∃ F ⊂ E$ un SEV de $E$ tel que $\mathcal{F} = \overrightarrow{a} + F$

On dit que $\mathcal{F}$ est le SEA de $E$ passant par $\overrightarrow{a}$ parallèle a $F$.

#### Théorème

**Soient $E,F$ des EV, soit $f  ∈\mathcal{L}(E,F)$, Soit $b  ∈F$**

**On note $\mathcal{S} = \{x  ∈E / f(x) = b\}$**

**Si $b ∉ \text{im}(f)$ alors $\mathcal{S} = \varnothing$,**

**Sinon, $\mathcal{S}$ est un SEA de $E$ de direction $\text{ker}(f)$**

#### Preuve

On suppose $b  ∈\text{im}(f)$

Donc $∃ x_0  ∈E / f(x_0) = b$

$x  ∈\mathcal{S} \iff f(x) = b$

Donc $f(x) = f(x_0) \iff f(x - x_0) = 0$

Donc $x - x_0  ∈\text{ker}(f)$

$$
\iff x  ∈x_0 + \text{ker}(f)
$$

Donc $\mathcal{S} = x_0 + \text{ker}(f)$

#### Remarque

$f(x) = b$ d'inconnue $x$ est une equation de type affine $x_0$ correspondant a une solution particulière et $\text{ker}(f)$  les solutions homogènes (car égal a 0).

### Droite, Plan, et hyperplan dans les espaces affines

#### Définition *droite*

Une droite affine $\mathcal{D}$ est un SEA de dimension 1.

$\mathcal{D}$ est une droite affine si et seulement si,
$$
∃ A  ∈\mathcal{E}, ∃ u  ∈E / u \neq 0
$$
$$
\mathcal{D} = A \tilde{+} \text{Vect}(u)
$$

Soient $A,B  ∈\mathcal{E} /A \neq B$, il existe une unique droite passant par $A,B$  notée $(AB) = A \tilde{+} \text{Vect}(\overrightarrow{AB})$ 

#### Définition *plan*

Un plan affine $\mathcal{P}$ est un SEA de dimension 2.

$\mathcal{P}$ est un plan affine si et seulement si,

$$
∃ A  ∈\mathcal{E}, ∃ u, v ∈E / u, v \text{ non-colinéaires et } \mathcal{P} = A \tilde{+} \text{Vect}(u, v)
$$

Il existe un unique plan affine passant par trois points $A,B,C$ affinement indépendents et est noté $(ABC) = A \tilde{+} \text{Vect}(\overrightarrow{AB}, \overrightarrow{AC})$.

SOit $\mathcal{H}$ un hyperplan affine, qui est un SEA de direction un hyperplan vectoriel.

$\mathcal{H}$ est un hyperplan affine si et seulement si:
$$
∃ A ∈\mathcal{E}, ∃ φ  ∈E^{*} / φ \neq 0, \mathcal{H} = A \tilde{+} \text{ker}(φ)
$$

### Intersection de SEA

#### Théorème

Une intersection se $SEA$ est soit vide soit un SEA (de direction l'intersection des directions)

#### Preuve

Soit $(\mathcal{F}_i)$ une famille de SEA de $\mathcal{E}$

$∀ i  ∈I, ∃ F_i$ un SEV de $E / \mathcal{F}_i$ soit de direction $F$

On pose
$$
\mathcal{F} = \bigcap_{i  ∈I} \mathcal{F}_i, F = \bigcap_{i  ∈I} F_i
$$

$F$ est un SEV de $E$

SI $\mathcal{F} \neq \varnothing$

$∃ A ∈\mathcal{F}$ et $A  ∈\mathcal{F_i}, ∀ i$

$\mathcal{F}_i = A \tilde{+} F_i$

$$
\mathcal{F} = \bigcap (A \tilde{+} F_i) = A \tilde{+} \bigcap F_i = A \tilde{+} F
$$

#### Remarque

En général:
$$
A ∩ (B + C) \neq A ∩B + A ∩ C
$$

Donc a mediter (par double inclusion l'égalité précédente)

### Des Exemples

Les SEA de $\mathbb{R}^{2}$ sont:

- Les points,
- Les droites,
- et le plan $\mathbb{R}^{2}$

Les SEA de $\mathbb{R}^3$ sont:

- Les points,
- Les droites
- Les plans,
- et $\mathbb{R}^3$

L'ensemble des solutions d'une equation differentielle linéaire, d'orde 1 a coéfficients continues sur un intervalle.
- une droite affine

Soit $I$ un intervalle, soient $a,f ∈C^{0}(I, \mathbb{R})$,

$$
\mathcal{S} = \{y  ∈\mathcal{D}(I, \mathbb{R}) / y' + ay = f\}
$$

On introduit $φ: \mathcal{D}(I, \mathbb{R}) \to \mathcal{F}(I, \mathbb{R})$

$$
φ y \mapsto y' + ay
$$

$\mathcal{S}$ est non-vide car l'équation differentielle admet au moins une solution (méthode de variation de la constante).

Donc $\mathcal{S}$ est un SEA de direction $\text{ker}( φ )$, l'ensemble des solutions a l'équation homogène, qui est un SEV de dimension 1.

L'ensemble des solutions d'une équation différentielle d'ordre 2, linéaire, a coéfficients constants, et a second membre continu sur un intervalle, est un plan affine.

(En éxercice)

L'ensemble des solutions d'un système linéaire, est soit vide, soit un SEA.

On considère $A  ∈\mathcal{M}_{n,p}(\mathbb{K})$ et $B ∈\mathcal{M}_{n,1}(\mathbb{K})$

On pose $\mathcal{S} = \{X  ∈\mathcal{M}_{1,p}(\mathbb{K}) / AX = B\}$

Soit $φ : \mathcal{M}_{1,p}(\mathbb{K}) \to \mathcal{M}_{n,1}(\mathbb{K})$

$$
φ : X \mapsto AX
$$

$φ$ est linéaire et le théorème permet de conclure.

Que dire de $\mathcal{S} = \{P  ∈\mathbb{R}_n[X] / \tilde{P}'(2) = 3\}$

On pose $φ : \mathbb{R}_n[X] \to \mathbb{R}$
$$
φ : P \mapsto \tilde{P}'(2)
$$

Si $n = 0, \mathcal{S} = \varnothing$ sinon, $3X  ∈\mathcal{S} \neq \varnothing$

$\mathcal{S}$ est un SEA affine de direction $\text{ker}( φ )$, qui est le noyeau d'une forme affine, donc $\mathcal{S}$ est un hyperplan affine.

Soient $a, b  ∈\mathbb{R}^3$

Que dire de $\mathcal{S} = \{x  ∈\mathbb{R}^3  / a \land x = b\}$

On pose $φ : \mathbb{R}^3 \to \mathbb{R}^3$

$$
φ :x \mapsto a \land x
$$


