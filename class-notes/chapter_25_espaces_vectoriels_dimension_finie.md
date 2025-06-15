# Chapitre 25: Espaces Vectoriels de dimension finie

## Espaces vectoriels de dimension finie et théorème fondamental

### Définition et exemples

#### Définition *Espace de dimension finie*

- Il possède une famille génératrice finie
- Sinon on dit que l'espace véctoriel est de dimension infinie

#### Exemples

- $\mathbb{R}^{n}$ est un $\mathbb{R}-$ev de dimension finie
- $\mathbb{K}_n[X]$ est un $\mathbb{K}-$ev de dimension finie
- $M_{n,p}(\mathbb{K})$ est un $\mathbb{K}-$ev de dimension finie

### Théorèmes fondamentaux

#### Lemme clé

Si un EV $E$ possède une famille libre génératrice de $n$
vecteurs alors toutes les familles libres de $E$ ont au plus $n$
vecteurs.

#### Preuve

Soit $(\overrightarrow{e_i})_{i  ∈I}$ une famille libre de $E$

Soient $\overrightarrow{f_1}, \overrightarrow{f_2}, \cdots, \overrightarrow{f_n}$ une famille génératrice

Il s'agit de prouver que $|I| \le n$

Supposons par l'absurde que $|I| > n \iff |I| \ge n+1$

La sous-famille $\overrightarrow{e_1}, \overrightarrow{e_2}, \cdots, \overrightarrow{e_{n+1}}$ est donc libre

Ainsi les $n+1$ vecteurs $\overrightarrow{e_1}, \cdots, \overrightarrow{e_{n+1}}$ sont combinaison linéaire
des $n$ vecteurs $\overrightarrow{f_1}, \cdots, \overrightarrow{f_n}$

D'après le théorème "Théorie de la dimension", la famille $\overrightarrow{e_1}, \cdots, \overrightarrow{e_{n+1}}$ est liée.

C'est absurde.

#### Théorème

"Théorème de la base incomplète"

Dans un EV de dimension finie, toute famille libre est complète en une base finie.

#### Preuve

Notons $E$ un EV, soit $\mathcal{G}$ une famille génératrice finie de $E$ Soit $L$ une famille libre de $E$.

$\mathcal{L}$ est nécéssairement fini en vertu du lemme clé.

On construit une base de $E$  en complétant la famille $\mathcal{L}$  par des vecteurs de $\mathcal{G}$ de la manière suivante:

Au départ $\mathcal{F} = \mathcal{L}$

- $\to$ si $\mathcal{F}$ est génératrice alors on arrète
- $\to$ sinon $\mathcal{F}$ n'est pas génératrice:

Ainsi $∃ \overrightarrow{x}  ∈\mathcal{G} / \overrightarrow{x} ∉ \text{Vect}(\mathcal{F})$

Sinon $∀\overrightarrow{x}  ∈\mathcal{G}, \overrightarrow{x} ∈\text{Vect}(\mathcal{G})$

Donc $\mathcal{G} ⊂ \text{Vect}(\mathcal{F})$

or $\text{Vect}(\mathcal{G}) = E \implies \text{Vect}(\mathcal{F}) = E$

Or $\mathcal{F}$ n'est pas génératrice donc cela est absurde.

On adjoint le vecteur $\overrightarrow{x}$ a $\mathcal{F}$

D'après le principe d'extension des familles libres, la famille $\mathcal{F}$ est libre tout au long de l'algorithme.

Si le procédé s'arrète avant épuisement de $\mathcal{G}$ alors $\mathcal{F}$ est génératrice, sinon il s
arrète après épuisement des vecteurs de $\mathcal{G}$. Dans ce cas $\mathcal{G}  ⊂\mathcal{F}$ Donc $\mathcal{F}$ est génératrice en tant que surfamille de $\mathcal{G}$ qui est génératrice.

Ainsi a la fin de l'algorithme, $\mathcal{F}$ est une base de $E$.

$\mathcal{F} ⊂ \mathcal{L} ∪ \mathcal{G}$

Ainsi $\mathcal{F}$ est finie.

#### Théorème

"Théorème de la base éxtraite"

Dans tout EV de dimension finie, de toute famille génératrice on peut extraire une base finie.

#### Preuve

Notons $E$ un EV, soit $\mathcal{G}$ une famille génératrice de $E$ 

On construit une base de $E$  en complétant la famille $\varnothing$  par des vecteurs de $\mathcal{G}$ de la manière suivante:

Au départ $\mathcal{F} = \varnothing$

- $\to$ si $\mathcal{F}$ est génératrice alors on arrète
- $\to$ sinon $\mathcal{F}$ n'est pas génératrice:

Ainsi $∃ \overrightarrow{x}  ∈\mathcal{G} / \overrightarrow{x} ∉ \text{Vect}(\mathcal{F})$

Sinon $∀\overrightarrow{x}  ∈\mathcal{G}, \overrightarrow{x} ∈\text{Vect}(\mathcal{G})$

Donc $\mathcal{G} ⊂ \text{Vect}(\mathcal{F})$

or $\text{Vect}(\mathcal{G}) = E \implies \text{Vect}(\mathcal{F}) = E$

Or $\mathcal{F}$ n'est pas génératrice donc cela est absurde.

On adjoint le vecteur $\overrightarrow{x}$ a $\mathcal{F}$

D'après le principe d'extension des familles libres, la famille $\mathcal{F}$ est libre tout au long de l'algorithme.

si l'algorithme ne s'arette pas alors on construit dans $E$ une famille libre infinie, cela contredit le lemme clé et que $E$ soit de dimension finie.

Si le procédé s'arrète avant épuisement de $\mathcal{G}$ alors $\mathcal{F}$ est génératrice, sinon il s
arrète après épuisement des vecteurs de $\mathcal{G}$. Dans ce cas $\mathcal{G}  = \mathcal{F}$ Donc $\mathcal{F}$ est génératrice.
Ainsi a la fin de l'algorithme, $\mathcal{F}$ est une base de $E$.

$\mathcal{F} ⊂ \mathcal{L} ∪ \mathcal{G}$

Ainsi $\mathcal{F}$ est finie car le procédé s'arrète en un nombre fini d'étapes.

#### Corollaire

Tout EV de dimension finie possède au mons une base finie.

### Preuve

Soit $\mathcal{G}$ une famille génératrice finie.

On extrait de $\mathcal{G}$ une base finie par le théorème de la base extraite.

#### Remarque

Ces trois théorèmes restent vrais, dans un EV de dimension infinie mais les preuves doivent être différentes et les bases obtenus sont infinie.

## Dimension d'un Espace Vectoriel de dimension finie

### Dimension

#### Définition-Théorème *Dimension*

Soit $E$ un $\mathbb{K}-$ev de dimension finie

Toutes les bases de $E$ ont le même nombre d'éléments, et ce nombre d'éléments commun est appélé dimension de $E$.

On le note $\text{dim}_{\mathbb{K}}(E)$ ou bien $\text{dim}(E)$ s'il n'y a pas d'ambiguité.

#### Preuve

Soient $(\overrightarrow{e_i})_{i  ∈I}$ et $(\overrightarrow{f_j})_{j ∈J}$ deux bases de $E$.

Elles sont finie par le lemme clé

On note $n = |I|$ et $p = |J|$

La famille $(\overrightarrow{e_i})$ est une famille génératrice constituée de $n$ vecteurs et $(\overrightarrow{f_j})$ est une famille libre de $p$ vecteurs

Donc par le lemme clé, $p \le n$ 

Or les bases jouent des roles symmétriques donc $n  \le p$

Ainsi $p = n$

#### Exemples

- $\text{dim}_{\mathbb{K}}(\mathbb{K}^{n}) = n$
- $\text{dim}_{\mathbb{R}}(\mathbb{R})  =1$
- $\text{dim}_{\mathbb{R}}(\mathbb{C}) = 2$
- $\text{dim}(\mathbb{K}_n[X]) = n+1$
- $\text{dim}(M_{n,p}(\mathbb{K})) = np$
- $\text{dim}(D_n(\mathbb{K})) = n$
- $\text{dim}(T_n^{+}(\mathbb{K})) = n(n+1)/2$
- $\text{dim}(T_n^{-}(\mathbb{K})) = n(n+1)/2$
- $\text{dim}(S_n(\mathbb{K})) = n(n+1)/2$
- $\text{dim}(A_n(\mathbb{K})) = n(n-1)/2$
- L'ensembles des suites arithmétiques sont de dimension $2$
- L'ensemble des solutions d'une équadif d'ordre 1, linéaire, homogène, a coéfficients continus sur un intervalle  est de dimension 1
- L'ensemble des solutions d'une équadif d'ordre 2 a coéfficients constants est de dimension 2.
- L'ensemble des suites vérifiant une relation de récurrence d'ordre 2 linéaire homogène a coéfficients constants est de dimension $2$

### Coordonnées composantes d'un vecteur dans une base

#### Définition-Théorème *Coordonnées composantes d'un vecteur*

Soit $E$ un EV avec $\text{dim}(E) = n \mathbb{N}^{*}$

Soit $B = (\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$ une base de $E$

$∀\overrightarrow{x}  ∈E, ∃ ! (λ _1, \cdots, λ _n)  ∈\mathbb{K}^{n} / \overrightarrow{x} = \sum_{k=1}^{n} λ _i \overrightarrow{e_i}$

$λ _1, \cdots, λ _n$ sont les Coordonnées de $\overrightarrow{x}$ dans la base $B$ et on note $\overrightarrow{x} = (λ _1, \cdots, λ _n)_B$

Existence: provient du fait que $B$ est génératrice

Unicité: Supposons qu'il y ai deux composnates possibles $λ _i$ et $μ _i$.

Donc $\overrightarrow{0_E} = \sum_{i=1}^{n} (λ _i - μ _i)$

Or $B$ est libre donc $∀i, λ _i - μ _i = 0$

#### Exemples

- Donner les coordonés de $P  ∈\mathbb{R}_n[X]$ dans la base $B = \left((X-a)^{k})\right)_{0 \le k \le n}$

Par la formule de taylor:
$$
P = \sum_{k=0}^{n} \frac{\tilde{P}^{(k)}(a)}{k!}(X-a)^{k}
$$

$$
P = \left(\frac{\tilde{P}^{(0)}(a)}{1!}, \cdots, \frac{\tilde{P}(a)^{(n)}}{n!}\right)_B$$

- Soient $x_0, \cdots, x_n in \mathbb{R}$ distincts et $L_0, \cdots, L_n$ les polynomes d'interpolation de lagrange associés a $x_0, \cdots, x_n$ Donner les coordonnés de $P$ dans la base $(L_0, \cdots, L_n)$

$$
P = (\tilde{P}(x_0), \cdots, \tilde{P}(x_n))_B
$$

### Théorèmes fondamentaux

#### Théorème

Soit $E$ un EV de dimesion $n$

- Toute famille libre possède au plus $n$ vecteurs
- Toute famille génératrice possède au moins $n$ vecteurs

#### Preuve

Soit $\mathcal{B} = (\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$ une base de $E$

Soit $\mathcal{L} = (\overrightarrow{f_1}, \cdots, \overrightarrow{f_p})$ une famille libre de $E$

$\mathcal{B}$ est génératrice donc par le lemme clé, $p \le n$.

Soit $\mathcal{G} = (\overrightarrow{g_1}, \cdots, \overrightarrow{g_p})$ une famille génératrice.

Par le lemme clé, $n \le p$ avec $\mathcal{B}$ étant une famille libre et $\mathcal{G}$ génératrice.

#### Corollaire

Soit $E$ un EV, de dimension $n$

- Toute famille libre de $n$ vecteurs de $E$ est une base
- Toute famille génératrice de $n$ vecteurs de $E$est une base

#### Preuve

Soit $\mathcal{L} = (\overrightarrow{e_1},\cdots, \overrightarrow{e_n})$ une famille libre de $E$.

Supposons $L$ non-génératrice

Alors $∃ \overrightarrow{x} ∈E / \overrightarrow{x}  ∉\text{Vect}(\mathcal{L})$

Donc $\mathcal{L}  ∪\{\overrightarrow{x}\}$ est une famille libre (par le principe d'extension des familles libres)

Or cette famille a $n+1$ vecteurs, elle est donc génératrice et c'est donc une base.

Il existe un vecteur combinaison linéaire des autres:
$$
∃ \overrightarrow{e_i}  ∈\text{Vect}(\overrightarrow{e_1}, \cdots, \overrightarrow{e_{i-1}}, \overrightarrow{e_{i+1}}, \cdots, \overrightarrow{e_n})
$$

Soit $\mathcal{G} = (\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$ une famille génératrice de $E$. Supposons que $\mathcal{G}$ soit liée. Ainsi

La famille $\overrightarrow{(e_k)_{k  ∈ [[1,n]] \backslash \{i\}}}$ est génératrice par réduction et est constituée de $n-1$ vecteurs ce qui contredit ce qui précède.

Ainsi $\mathcal{G}$ est une base. 

#### Exemple

Soit $a  ∈\mathbb{R}, n  ∈\mathbb{N}$

Montrons que $((X- a)^{k})$ est une base de $\mathbb{R}_n[X]$

La famille est génératrice et

$∀ k, \text{deg}(X - a)^{k} = k$ donc la famille est libre etant constituée de polynomes de degré 2-a-2 distincts sans le polynome nul.

Or la famille libre $(X-a)^{k}$ contient $n+1$ vecteurs, elle est donc génératrice et est une base.

## Dimensions et Opérations sur les Sous-Espaces Véctoriels

### Dimension d'un sous-espace véctoriel

#### Théorème

Soit $E$ un $\mathbb{K}-$ev de dimension finie, soit $F$ un SEV de $E$.
$F$ est de dimension finie et $\text{dim}(F) \le \text{dim}(E)$.

De plus,
$$
F = E \iff \text{dim}(F) = \text{dim}(E)
$$

#### Preuve

Si $F = \{\overrightarrow{0_E}\}$ alors $\text{dim}(F) = 0$

Sinon $\overrightarrow{0_E} ∈F \land ∃ \overrightarrow{x} ∈ F / \overrightarrow{x} \neq \overrightarrow{0_E}$

Dans ce cas on note $\mathcal{N}$ l'ensemble des nombres d'elements des familles de $F$ libres et non-vides.

Or une famille libre de $F$ est une famille libre de $E$ ainsi $\mathcal{N}$ est majoré par $\text{dim}(E)$.

Par un axiome de Peano, $\mathcal{N}$ possède un maximum noté $p$.

Soient $(\overrightarrow{e_1}, \cdots, \overrightarrow{e_p})$ une famille libre de vecteurs de $F$.

Par l'absurde, si $(\overrightarrow{e_1}, \cdots, \overrightarrow{e_p})$ n'est pas génératrice dans $F$ alors il existe $\overrightarrow{x}  ∈F$ tel que $\overrightarrow{x}  ∉\text{Vect}(\overrightarrow{e_1}, \cdots, \overrightarrow{e_p})$

D'après le principe d
extension des familles libres, on a que $(\overrightarrow{e_1}, \cdots, \overrightarrow{e_p}, \overrightarrow{x})$ est libre, et contient $p+1$ vecteurs, ce qui contredit le fait que $p$ soit le maximum de $\mathcal{N}$.

Ainsi $(\overrightarrow{e_1}, \cdots, \overrightarrow{e_p})$ est une base de $F$ et $F$ est de dimension $p$.

Si $F  = E$ il est clair que $\text{dim}(F) = \text{dim}(E)$.

Montrons l'autre sens:

Soit une base $\mathcal{B}(\overrightarrow{e_1}, \cdots, \overrightarrow{e_p})$ de $F$. Celle-ci est libre dans $F$ donc dans $E$.

Or cette famille contient $p$ vecteurs donc elle est génératrice sur $E$ et ainsi $E = \text{Vect}(\mathcal{B}) = F$

#### Exemples

- On appelle droite vectorielle d'un EV un SEV de dimension 1: c'est a dire un SEV engendré par un vecteur non-nul.

Ainsi $D$ est une droite vectorielle de $E$ si est seulement si:
$$
∃ \overrightarrow{u}  ∈E / \overrightarrow{u} \neq \overrightarrow{0_E} \land \text{Vect}(\overrightarrow{u}) = D
$$

- On appelle plan d'un EV tout SEV de dimension 2: c'est a dire tout SEV engendré par deux vecteurs non-colinéaires.

Ainsi $P$ est un plan de $E$ si et seulement si:
$$
∃ \overrightarrow{u}, \overrightarrow{v}  ∈E /  ∀λ  ∈\mathbb{K}, \overrightarrow{u} \neq λ \overrightarrow{v} \land \text{Vect}(\overrightarrow{u}, \overrightarrow{v}) = P
$$

#### Corollaire

Tout SEV d'un EV de dimension finie admet au moins un supplémentaire.

#### Preuve

Soit $E$ un SEV de dimension finie $n$

Soit $F$ un SEV de $E$.

$F$ est donc de dimension finie, disons $p$.

Soit donc $\mathcal{F} = (\overrightarrow{f_1}, \cdots, \overrightarrow{f_p})$ une base de $F$.

$\mathcal{F}$ est une famille libre de vecteurs de $E$.

Par le théorème de la base incomplète, on complète la famille $\mathcal{F}$ en une base $\mathcal{E}$ de $E$.

On a donc un supplémentaire $S = \text{Vect}(\mathcal{E} \backslash \mathcal{F})$

Comme $\mathcal{F}$ est libre la somme $F\oplus S$ est directe.

Comme $\mathcal{E}$ est génératrice, $E= F+S$.

### Dimension d'un produit cartésien d'espaces véctoriels

#### Théorème

Soit $E, F$  deux EV de dimension finie

Alors,
$$
\text{dim}(E \times F) = \text{dim}(E) + \text{dim}(F)
$$

#### Preuve

On note $n = \text{dim}(E)$

Soit $\mathcal{B}_1 = (\overrightarrow{e_1}, \cdots, \overrightarrow{e_n})$ une base de $E$ 

On note $p = \text{dim}(F)$

Soit $\mathcal{B}_2 = (\overrightarrow{f_1}, \cdots, \overrightarrow{f_p})$ une base de $F$

Soit
$$
\mathcal{B} = \left((\overrightarrow{e_1}, \overrightarrow{0_F}), \cdots, (\overrightarrow{e_n}, \overrightarrow{0_F}), (\overrightarrow{0_E}, \overrightarrow{f_1}), \cdots, (\overrightarrow{0_E}, \overrightarrow{f_p})\right)
$$

une base de $E \times F$

Vérifions la liberté de $\mathcal{B}$

Soient $λ _1, \cdots, λ _n, μ _1, \cdots, μ _ p  ∈\mathbb{K}$

tels que:
$$
\sum_{i=0}^{n} λ _i (\overrightarrow{e_i}, \overrightarrow{0_F}) + \sum_{i=0}^{p} μ _i (\overrightarrow{0_E}, \overrightarrow{f_i}) = (\overrightarrow{0_E}, \overrightarrow{0_F})
$$

Ainsi:

$$
\left(\sum_{i=0}^{n} λ _i \overrightarrow{e_i}, \sum_{i=0}^{p} μ _i \overrightarrow{f_i} \right) = (\overrightarrow{0_E}, \overrightarrow{0_F})
$$


$$
\implies
\begin{cases}
\sum_{i=0}^{n} λ _i \overrightarrow{e_i} = \overrightarrow{0_E} \\
\sum_{i=0}^{p} μ _i \overrightarrow{f_i} = \overrightarrow{0_F}\end{cases}
$$

ainsi par la liberté de $\mathcal{B_1}$ et $\mathcal{B_2}$ on a que $∀i, λ _i = μ _i = 0$

Montrons que $\mathcal{B}$ est génératrice:

Soient $(\overrightarrow{x}, \overrightarrow{y})  ∈E \times F$

$\mathcal{B_1}$ étant génératrice dans $E$:
$$
\overrightarrow{x} = \sum λ _i \overrightarrow{e_i}
$$

$\mathcal{B_2}$ étant génératrice dans $F$:
$$
\overrightarrow{y} = \sum μ _i \overrightarrow{f_i}
$$

Ainsi
$$
(\overrightarrow{x}, \overrightarrow{y}) = \left(\sum λ _i \overrightarrow{ e_i}, \sum μ _i \overrightarrow{f_i}\right)
$$

Donc $E \times F$ est de dimension finie et $\text{dim}(E \times F) = |\mathcal{B}| = \text{dim}(E) + \text{dim}(F)$

#### Corollaire

Si $E_1, \cdots, E_p$ sont des EC de dimension finies alors $\prod E_i$ est un EV de dimension finie et:
$$
\text{dim}\left(\prod_{i=1}^{p} E_i\right) = \sum_{i=1}^{p} \text{dim}(E_i)
$$

#### Preuve

par récurrence sur $p$

### Dimension d'une somme de deux SEV

#### Théorème

Si $E$ est un EV de dimension finie et si $F, G$ sont des SEV de $E$ supplémentaires alors $\text{dim}(E) = \text{dim}(F) + \text{dim}(G)$.

#### Preuve

Soit $\mathcal{B_F}$ une base de $F$
Soit $\mathcal{B_G}$ une base de $G$

Soit $\mathcal{B} = \mathcal{B_F} ∪\mathcal{B_G}$ une base de $E$

donc $\text{dim}(E) = |\mathcal{B_F}  ∪\mathcal{B_G}|$ 
$= |\mathcal{B_F}|  + |\mathcal{B_G}| - |\mathcal{B_F} ∩\mathcal{B_G}| = \text{dim}(F) + \text{dim}(G)$.

#### Remarque
$$
\text{dim}(F \oplus G) = \text{dim}(F) + \text{dim}(G)
$$

#### Théorème

On suppose que $E$ est de dimension finie

et $F, G$ des SEV de $E$.
$$
\text{dim}(F + G) = \text{dim}(F) + \text{dim}(G) - \text{dim}(F ∩ G)
$$

C'est la Formule de Grassman

#### Preuve

$F ∩ G$ est un SEV de $F$ et possède un supplémentaire noté $S$.

On a $F = F ∩ G \oplus S$

Montrons que $G \oplus S = F + G$

- $G  ⊂F +G$
- $S  ⊂F  ⊂F + G$

Soit $\overrightarrow{x}  ∈ F  +G  \iff ∃ \overrightarrow{f}  ∈F, \overrightarrow{g}  ∈G / \overrightarrow{x} = \overrightarrow{f} + \overrightarrow{g}$

Or $\overrightarrow{f} ∈ F = F ∩ G  + S$ Donc $∃ \overrightarrow{y}  ∈F ∩G, \overrightarrow{z} ∈S / \overrightarrow{f} = \overrightarrow{y} + \overrightarrow{z}$

$$
\overrightarrow{x} = (\overrightarrow{y} + \overrightarrow{g}) + \overrightarrow{z}
$$

or $\overrightarrow{y} + \overrightarrow{g} ∈G$ et $\overrightarrow{z}  ∈S$ donc $\overrightarrow{x} ∈G + S$

On a donc l'égalité:
$$
G + S = F + G
$$

puis:
$$
G ∩S = G ∩ (S ∩F)= (F ∩G) ∩ S = \{\overrightarrow{0_E}\}
$$

Ainsi:
$$
G \oplus S = F + G
$$

Donc $\text{dim}(F) = \text{dim}(F ∩G) + \text{dim}(S)$

et $\text{dim}(F+G) = \text{dim}(S) + \text{dim}(G)$

D'ou:
$$
\text{dim}(F+G) = \text{dim}(F) + \text{dim}(G) - \text{dim}(F ∩ G)
$$

#### Corollaire

Si $E = F+G$ alors
$$
\text{dim}(E) \le \text{dim}(F) + \text{dim}(G)
$$

Avec égalité si et seulement si $F + G$ est directe (i.e. ils sont supplémentaires) 

#### Corollaire

"Caractérisation dimensionelle de la supplémantarité de 2 SEV"

Soit $E$, un EV, et $F, G$ deux SEV de $E$.

$F,G$ sont supplémentaires si  et seulement si:

deux des trois points usivants sont vrais:

1. $E ⊂ F + G$
2. $F  ∩G  ⊂ \{\overrightarrow{0_E}\}$
3. $\text{dim}(E) = \text{dim}(F) + \text{dim}(G)$

#### Exemple: "La bonne méthode pour prouver que $S_n(\mathbb{K}) \oplus A_n(\mathbb{K}) = M_n(\mathbb{K})$ "

Soit $M ∈S_n ∩ A_n$
$M^{\top} = M$ et $M^{top} = -M$

Ainsi $M = -M$ et $M = 0$

$$
n^2 = \frac{n(n+1)}{2} + \frac{n(n-1)}{2}
$$

$$
\text{dim}(M_n) = \text{dim}(S_n) + \text{dim}(A_n)
$$

## Rang d'une famille de Vecteurs

#### Définition *Rang de famille de vecteurs*

Soit $E$ un EV et $\overrightarrow{x_1}, \cdots, \overrightarrow{x_p}$  une famille de vecteurs de $E$.

On appelle rang de $\overrightarrow{x_1}, \cdots, \overrightarrow{x_p}$ la dimension de l'espace vectoriel engendré par ces vecteurs
$$
\text{rg}(\overrightarrow{x_1}, \cdots, \overrightarrow{x_p}) = \text{dim}(\text{Vect}(\overrightarrow{x_1}, \cdots, \overrightarrow{x_p}))
$$

#### Propriété

$$
\text{rg}(\overrightarrow{x_1}, \cdots, \overrightarrow{x_p}) \le p
$$

Avec égalité si la famille est libre

#### Preuve

Soit $F = \text{Vect}(\overrightarrow{x_1}, \cdots, \overrightarrow{x_p})$

Or $\overrightarrow{x_1}, \cdots, \overrightarrow{x_p}$ est génératrice de $F$, donc $p \ge \text{dim}(F)$

" $\implies$ " 
Supposons que $\text{dim}(F) = p$

Alors $\overrightarrow{x_1}, \cdots, \overrightarrow{x_p}$ est génératrice contenant $p$ vecteurs, elle est donc une base, et donc aussi libre.

" $\impliedby$ "
supposons $\overrightarrow{x_1}, \cdots, \overrightarrow{x_p}$ libre.

Elle est génératrice de $F$ donc $\text{dim}(F) = p$

#### Propriété

On suppose $E$ de dimension finie.

Alors
$$
\text{rg}(\overrightarrow{x_1}, \cdots, \overrightarrow{x_p}) \le \text{dim}(E)
$$

avec égalité si et seulement si $(\overrightarrow{x_1}, \cdots, \overrightarrow{x_p})$ est génératrice

#### Preuve

On pose $F = \text{Vect}(\overrightarrow{x_1}, \cdots, \overrightarrow{x_p})$

$F$ est un SEV de $E$ donc $\text{dim}(F) \le \text{dim}(E)$

$\implies$ si $\text{dim}(F) = \text{dim}(E)$ alors $F = E$ et $(\overrightarrow{x_1}, \cdots, \overrightarrow{x_p})$ est génératrice.

$\impliedby$ Si $(\overrightarrow{x_1}, \cdots, \overrightarrow{x_p})$   est génératrice alors $F = E$ et $\text{dim}(F) = \text{dim}(E)$.

#### Corollaire

On prends $E$ de dimension finie $n$.

$$
\text{rg}(\overrightarrow{x_1}, \cdots, \overrightarrow{x_n}) = \text{dim}(E) \iff (\overrightarrow{x_1}, \cdots, \overrightarrow{x_n}) \text{ est une base de } E
$$

#### Remarque

Comment calculer le rang d'une famille de vecteurs?

Soient la famille $(\overrightarrow{x_k})_{k  ∈1..p}$

si $(\overrightarrow{x_k})$ est libre alors $\text{rg} = p$

Sinon $∃ i / \overrightarrow{x_i} ∈ \text{Vect}(\overrightarrow{x_k})_{k \neq i})$

Donc $\text{rg}(\overrightarrow{x_k}) = \text{rg}(\overrightarrow{x_{k\neq i}})$ 
