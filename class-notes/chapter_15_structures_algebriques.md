# Chapitre 15: Structures Algébriques Usuelles

## Loi de composition interne

### Premierre définition et exemples

#### Définition *loi de composition interne*

On appelle loi de composition interne sur $E$ toute application de $E \times E$ dans $E$.

Si on note $\top$ cette application et si $x, y, ∈ E$ alors on note $x \top y$ l'image du couple $(x,y)$ par l'application $\top$.

#### Exemple

- L'addition $+$ est une loi de composition interne sur $\mathbb{R}$

- La multiplication $\times$ est une loi de composition interne sur $\mathbb{R}$

- La réunion / l'intersection $\cup / \cap$ sur un ensemble $X$, est $P(X)$

- La composition d'applications $\circ$  est une loi de composition interne sur $X^{X}$.

- Le produit vectoriel $\land$ est une loi de composition interne sur $\mathbb{R}^{3}$

- La somme parallele noté $//$ est une loi de composition interne sur $R^{+*}$ ($a // b = \frac{ab}{a+b}$)

### Diverses propriétés

Dans cette partie $E$ désigne un ensemble et $\top$ désigne une loi de composition interne sur $E$.

#### Commutativité

#### Définition *Commutatif*

Soient $a, b ∈ E

On a $\top$ commutatif  si $a \top b = b \top a$

#### Exemple

- $+, \times$ sont commutatifs

- $-$ ne l'est pas

- $\cup / \cap$ sont commutatifs

- la composition d'applications $\circ$ ne l'est que dans certains cas particuliers.

- le produit vectoriel ne l'est pas:

$$
\left(
\begin{matrix}
1 \\ 0 \\ 0
\end{matrix}
\right)
\land
\left(
\begin{matrix}
0 \\ 1 \\ 0
\end{matrix}
\right)
= 
\left(
\begin{matrix}
0 \\ 0 \\ 1
\end{matrix}
\right)
$$

$$
\begin{pmatrix}
0 \\ 1 \\ 0
\end{pmatrix}
\land
\begin{pmatrix}
1 \\ 0 \\ 0
\end{pmatrix}
= 
\begin{pmatrix}
0 \\ 0 \\ -1
\end{pmatrix}
$$


#### Associativité

#### Définition *associatif*

$\top$ est associatif si:

$$
a \top (b \top c) = (a \top b) \top c
$$

#### Exemples

- $+, \times, \cup, \cap$ sont associatives 
- $-$ ne l'est pas
- $\circ$ l'est
- $\land$ ne l'est pas:

$$
\left(
\left(
    \begin{matrix}
    1 \\ 0 \\ 0
    \end{matrix}
    \right)
\land
    \left(
        \begin{matrix}
        0 \\ 1 \\ 0
        \end{matrix}
        \right)      
\right)
\land
\left(
    \begin{matrix}
0 \\ 1 \\ 0
    \end{matrix}
    \right)
    =
    \left(
        \begin{matrix}
1 \\ 0 \\ 0
        \end{matrix}
      \right)
$$

$$
\left(
    \begin{matrix}
    1 \\ 0 \\ 0
    \end{matrix}
    \right)

\land
\left(
    \left(
        \begin{matrix}
        0 \\ 1 \\ 0
        \end{matrix}
        \right)      
\land
\left(
    \begin{matrix}
0 \\ 1 \\ 0
    \end{matrix}
    \right)
\right)
    =
    \left(
        \begin{matrix}
0 \\ 0 \\ 0
        \end{matrix}
      \right)
$$

- $//$ est associative 


#### Partie stable

#### Définition *partie stable*

On dit que $A ⊂ E$ est stable si $∀ a, b ∈ A, a \top b ∈ A$  

#### Définition *Element Neutre*

On dit que $\top$ possede un element n'eutre sur $E$ si:
$$
∃ e ∈ E / ∀ x ∈ E, (x \top e = e \top x = x)
$$

L'element neutre est **unique**.

#### Preuve de l'unicité

Soit $e, e'$ deux éléments neutres 

$$
e = e \top e' = e' \iff e = e'
$$

#### Exemples

- $\varnothing$ pour $\cup$ et $X$ pour $\cap$
- $\text{Id}_X$ pour $\circ$
- $\land$ n'en possède pas
- $//$ non plus


#### Invariabilité

On suppose que $\top$ est **associative** et possède un élement neutre noté $e$

#### Définition

Soit $x ∈ E$ On dit que $x$ est invariable pour $\top$.

$$
∃ y ∈ E / x \top y = e \land y \top x = e
$$

$y$ s'apelle alors l'inverse de $x$ noté $x^{-1}$

#### Remarques

- pour conclure l'existence d'un inverse il faut vérifier les DEUX relations
- si $x^{-1}$ exitse alors $x$ doit être inversible.
- si $\top$ n'est pas associative elle peut admettre pplusieurs inverses. 

#### Propriété

Soit $x, y$ on a : $(x^{-1})^{-1} = x$ et $(x \top y) ^{ -1} = y^{-1} \top x^{-1}$   


#### Exemples
 
- $+$ si $x$ appartient a $\mathbb{R}$ alors $x$ est inversible d'inverse $-x$
- $\times$ si $z ∈ \mathbb{C}$ alors $z$ est inversible si $z \neq 0$ d'inverse $\frac{1}{z}$     
- Dans $(X^{X}, \circ)$ $f$ est inversible si et seulement si $f$ est bijective.   

Calcul des inversibles de $(P(X), \cup)$ 

#### Remarque

L'élément neutre est toujours inversible et son inverse est lui-même.

#### Distributivité

#### Définition *distributif*

Soit $(E, \oplus, \otimes)$

Dire que $\oplus$ est distributif par rapport a $\otimes$ veut dire que:
$$
∀ a, b, c ∈ E, a \oplus (b \otimes c) = (a \oplus b) \otimes (a \oplus c)
\text{ et }(b \otimes c)  \oplus a = (a \oplus b) \otimes (a \oplus c)
$$

#### Exemples

- Dans $\mathbb{C}$, on a $\times$ distributif par rapport a $+$ mais pas l'inverse.   

- $\circ, +$ ne sont pas distributives. 

## Structures de groupe

### Groupe

#### Définition *un Groupe*

On dit que $(G, \top)$ est un groupe si 

- $G$ est un ensemble
- $\top$ est une LCI (Loi de composition interne)
- $\top$ doit être associatif
- $\top$ doit posseder un élément neutre
- $∀ x ∈ G$ il existe $x^{-1}$ pour la loi $\top$

SI en plus, $\top$  est commutative on dit qu'on a un groupe *abélien* ou un groupe *commutatif*.

#### Exemples

- $(\mathbb{Z}, +)$ est un groupe abélien
- $(\mathbb{N}, +)$ n'en est pas un car les $x > 0$  ne sont pas inversibles
- $(\mathbb{R}^{+}, \times)$ est un groupe abélien
- $(\mathbb{R}, \times)$ n'en est pas un car 0 n'est pas inversible
- $(\mathbb{D}, +) , (\mathbb{Q}, +), (\mathbb{R}, +)$  sont tous abéliens
- $(\mathbb{Q}^{*}, \times), (\mathbb{C}^{*}, \times)$ sont abéliens
- $(\mathbb{Z} \backslash \{0\}, \times)$ ne l'est pas car $∀ x, |x| ∈ \mathbb{N}^{*} \backslash \{1\}$
- $(\mathbb{R}^{-*}, \times)$ ne l'est pas car $\times$ n'est pas une LCI sur $\mathbb{R}^{-*}$ (pas d'élément neutre et $x, y ∈ \mathbb{R}^{-*} \implies xy ∉ \mathbb{R}^{-*}$ )

Si $X$ est un ensemble quelconque et si $(G, \top)$ est un groupe alors $(X^{G}, \top)$   est un groupe.

### Produit de groupe

#### Théorème

Soit $(G_1, \top_1)$ et $(G_2, \top_2)$  deux groupes.

On pose $\top$ l'application qui va de $G_1 \times G_2$ dans $G_1 \times G_2$

$$
\top : G_1 \times G_2 \to G_1 \times G_2 \\
((x_1, x_2) , (y_1, y_2)) \mapsto (x_1 \top_1 y_1), (x_2, \top_2 y_2)
$$

Alors $(G_1 \times G_2, \top)$ est un groupe.

De plus si $(G_1, \top_1)$ et $(G_2, \top_2)$ sont abéliens alors $(G_1 \times G_2, \top)$ est abélien.

### Sous-groupes

#### Définition *sous-groupe*

Soit $(G, \top)$ un groupe, et $H ⊂ G$.

On dit que $(H, \top)$ est un sous-groupe de $(G, \top)$ si:

1. $e ∈ H$
2. $∀ x,y ∈ H, x \top y ∈ H$
3. $∀ x ∈ H, \overbrace{x^{-1}}^{\text{possible car tt les elem sont inversibles (groupe)}} ∈ H$   

#### Exemples

- $(\mathbb{C}, +)$ possède les sous-groupes $\mathbb{Z}, \mathbb{D}, \mathbb{Q}, \mathbb{R}$

#### Théorème

Si $H$ est un sous groupe de $(G, \top)$ alors $(H, \top)$ est un groupe.

Si $(G, \top)$ est abélien alors $(H, \top)$ est abélien

#### Preuve

- $∀ x,y ∈ H, x \top y ∈ H$ donc $\top_{| H^2}^{|H}$ noté toujours $\top$ est une loi de composition interne sur $H$.
- $e ∈ H$ par hypothèse et $∀ x ∈ G, x \top e = e \top x = x$ donc $∀ x ∈ H, x \top e = e \top x = x$ donc $H$ possède un élément neutre.   
- $\top$ est associative sur $G$ donc sur $H$
- Soit $x ∈ H$ $x ∈ G$ donc $x^{-1}$ existe. Or par hypothèse $x^{-1 ∈ H}$
Or $x \top x^{-1} = x^{-1} \top x = e$ donc $x$ est inversible.
- Si $G$ abélien alors $H$ l'est car si $\top$ est commutative sur $G alors elle l'est sur $H$.              

#### Théorème "Caractérisation des sous-groupes"

Soit $(G, \top)$ un groupe, et $H ⊂ G$.

$$
(H) \text{ est un sous groupe de } (G, \top) \iff H \neq \varnothing, \text{ et } ∀ x, y, ∈ H, x^{-1} \top y ∈ H
$$

" $\implies$ " :

- $H \neq \varnothing$ car $e ∈ H$
- Soient $x, y ∈ H$ on a $x^{-1} ∈ H$ donc $x^{-1} \top y ∈ H$

" $\impliedby$ " :

- $H \neq \varnothing \implies ∃ x_0 ∈ H$
- $x^{-1} = x^{-1} \top e ∈ H$
- Soient $x, y ∈ H (x^{-1})^{-1} \top y ∈ H$  

#### Exemples

#### Théorème

$∀ n ∈ \mathbb{N}^{*}, \mathbb{U}_n$ est un sous groupe de $(\mathbb{U}, \times)$

#### Preuve

- $\mathbb{U} ⊂ \mathbb{C}^{*}$ et $(\mathbb{C}^{*}, \times)$ est un groupe.
- $\mathbb{U} \neq \varnothing, 1 ∈ \mathbb{U}$
- Soient $z, z' ∈ \mathbb{U}$
- $|\frac{1}{z} \times z'| = 1 \iff \frac{1}{z} \times z' ∈ \mathbb{U}$

Donc $\mathbb{U}$ est un sous-groupe de $(C^{*}, \times)$

- $\mathbb{U}_n ⊂ \mathbb{U}$
- $1 ∈ \mathbb{U}_n \iff \mathbb{U}_n \neq \varnothing$
- Soient $z, z' ∈ \mathbb{U}_n$
- $|(\frac{1}{z} \times z')^{n}| = 1$ donc $\frac{1}{z} \times z' ∈ \mathbb{U}_n$.

#### Définition *permutation d'un ensemble*

On appelle permutation de $X$:

Toute application bijective de $X$ dans $X$.

On note $S_X$ l'ensemble des permutations de $X$

#### Théorème

$(S_X, \circ)$ est un groupe.

#### Preuve

- Soient $f,g ∈ S_X$ $f \circ g$ est bijective en tant que composée de deux applications bijectives. Donc $f \circ g ∈ S_X$ on a donc bien une loi de composition interne sur $S_X$.
- $\circ$ est associative sur $S_X$ car elle l'est sur $X^{X}$
- $∀ f ∈ S_X, f \circ \text{Id}_X = \text{Id}_X \circ f = f$ et $\text{Id}_X \circ \text{Id}_X = \text{Id}_X$ donc $\text{Id}_X ∈ S_X$ et est l'element neutre de $\circ$.
- Soit $f ∈ S_X$ On sait que $f$ est bijective donc $f \circ f^{-1} = \text{Id}_X ∈ S_X$   
- $f^{-1} ∈ S_X$ donc $(S_X, \circ)$ est un groupe. 

## Morphismes de groupes

Soient $(G, \top)$ et $(H, \perp)$ deux groupes.

on note $e$ l'element neutre de $(G, \top)$
et $e'$ celui de $(H, \perp)$    


#### Définition *morphisme d'un groupe*

On dit qu'une application $φ : E \to F$ est un morphisme de groupes de $(G, \top)$ dans $(H, \perp)$ si:
$$
∀ x, y ∈ G, φ (x \top y) = φ (x) \perp φ (y)
$$ 

#### Exemples

- $\ln$ est un morphisme de $(\mathbb{R}^{+*}, \times)$ dans $(\mathbb{R}, +)$
- $\exp$ est un morphisme de $(\mathbb{C}, +)$ dans $(\mathbb{C}^{*}, \times)$
- la conjugaison complexe, est un morphisme de $(\mathbb{C}, +)$ dans $(\mathbb{C}, +)$

#### Propriété

- $φ (e) = φ (e')$
- $∀ x ∈ G, φ (x^{-1}) = (φ(x))^{-1}$

$$
φ e \perp φ e = φ e \\
(φ e \perp φ e) \perp φ e ^{-1} = φe \perp φ e^{-1} \\
= e'
$$

$$
φ (x \top x^{-1}) = φ (e) = e' \\
= φ (x) \perp φ x ^{-1}
$$

#### Théorème

Soit $φ : (G, \top) \to (H, \perp) $ un morphisme de deux groupes.

Si $G'$ est un sous groupe de $(G, \top)$ alors $φ (G')$ est un sous groupe de $(H, \perp)$ (idem pour $(H, \perp)$ mais avec $φ ^{-1}$ )   

#### Preuve

- $φ (G') ⊂ H$ et $(H, \perp)$ est un groupe.
- $e' = φ (e)$ avec $e ∈ G'$ donc $e' ∈ H$
- Soient $x, y ∈ φ (G')$  donc $∃ x', y' ∈ G' / φ (x') = x$ et $φ (y') = y$
- $x^{-1} \perp y = φ (x')$
$$
x^{-1} \perp y = φ (x') ^{-1} \perp φ (y') \\
x^{-1} \perp y = φ (x'^{-1}) \perp φ (y') \\
x^{-1} \perp y = φ (x'^{-1} \top y') ∈ φ (G')
$$

Donc $φ (G')$ est un sous groupe de $(H, \perp)$.

(idem pour $(H, \perp)$ avec $φ ^{-1}$  )

#### Définition *Morphisme de Groupe*

Soit $φ :  G \to H$ un morphisme de groupes 

On note:
- $\text{Im}( φ ) = \{ φ (x) / x ∈ G \}$
- $\text{Ker}( φ ) = \{ x ∈ G / φ (x) = e' \} = φ ^{-1} ( \{ e \} )$

#### Corollaire
- $\text{Im}( φ )$ est un sous-groupe de $(H, \perp)$
- $\text{Ker}( φ )$ est un sous groupe de $(G, \top)$    

#### Théorème
$φ $ est surjective si et seulement si $\text{Im}( φ ) = H$
$φ $ est injective si et seulement si $\text{Ker}( φ ) = \{e\}$

#### Preuve

Montrons l'injectvivité:

" $\implies$ ": On suppose que $φ $ est injective

On sait que $φ (e) = e'$ donc $e ∈ \text{Ker} ( φ )$

Soit $x ∈ \text{Ker}( φ )$

On a $φ (x) = e'$ or $φ (e) = e'$ donc par injectivité on a:
$$
x = e
$$

Ainsi $\text{Ker}( φ ) = \{e\}$ 

" $\impliedby$ ": Soient $x, y ∈ G / φ (x) = φ (y)$

$$
φ (x^{-1} \top y) = φ (x^{-1}) \perp φ (y) \\
= φ (x) ^{-1} \perp φ (y) \\
= φ (y) ^{-1} \perp φ (y) \\
= e'
$$

Donc $x^{-1} \top y ∈ \text{Ker}( φ )$ Donc comme $\text{card}(\text{Ker}( φ )) = 1$ on a $x = y$   

#### Définition *Isomorphisme de Groupe*
C'est un morphisme de groupe bijectif

#### Exemples
- $\ln$ en est un isomorphisme de $(\mathbb{R}^{+*}, \times)$ dans $(\mathbb{R}, +)$
- $\exp$ en est un morphisme de $(\mathbb{C}, +)$ dans $(\mathbb{C}^{*}, \times)$ (surjectif mais non-injectif)
- $z \mapsto \overline{z}$ est un isomorphisme involutif de $(\mathbb{C}, +)$ dans lui-même. (bijectif involutif)
- $\Re$ et $\Im$ sont des morphismes de $(\mathbb{C}, +)$ dans $(\mathbb{C}, +)$ (ni injectifs ni surjectifs)      

## Structure d'Anneau

### Anneau

#### Définition *Anneau*

On dit que $(A, +, \times)$ est un anneau, si:

- $A$ est un ensemble
- $+, \times$ deux lois de composition interne sur $A$.
- $(A, +)$ doit être un groupe abélien
- $\times$ doit être associative sur $A$
- $\times$ doit posseder un element neutre sur $A$
- et $\times$ doit être associative par rapport a $+$         

- Si en plus, $\times$ est commutative sur $A$ alors $(A, +, \times)$ est un anneau commutatif.   

#### Remarque

- On noteras $0_A$ le neutre pour $+$ et $1_A$ pour $\times$

#### Exemples
- $(\mathbb{C}, +, \times), (\mathbb{R}, +, \times), (\mathbb{Q}, +, \times), (\mathbb{D}, +, \times), (\mathbb{Z}, +, \times)$ sont des anneaux comutatifs
- $(\mathbb{R}^{\mathbb{N}}, +, \times)$ est un anneau commutatif
Plus généralement, si $X$ est un ensemble quelconque et si  
- $(A, +, \times)$ est un anneau alors $(X^{A}, +, \times)$ est un anneau
En particulier $(\mathbb{R}^{\mathbb{R}}, +, \times)$

- $(\mathbb{R}^{\mathbb{R}}, +, \circ)$ n'est pas un anneau car $\circ$ n'est pas distributive par rapport a $+$ du coté gauche.  

### Sous Anneau

#### Définition *Sous-anneau*

Soit $(A, +, \times)$ un anneau et $B ⊂ A$

On dit que $B$ est un sous anneau de $(A, + , \times)$ si 
- $(B, +)$ soit un sous-groupe de $(A, +)$
- $1_A ∈ B$
- $∀ x, y ∈ B, x \times y ∈ B$

#### Théorème
Si $B$ est un sous-anneau d'un anneau $(A, +, \times)$ alors $(B, +, \times)$ est un anneau

De plus si $(A, +, \times)$ est commutatif alors $(B, +, \times)$ est commutatif  

#### Théorème "Caractérisation des Anneaux"

On considère $B ⊂ (A, +, \times)$ Donc $B$ est un sous anneau de $(A, +, \times)$

si et seulement si:

- $∀ x , y ∈ B, x - y ∈ B$
- $1_A ∈ B$
- $∀ x,y ∈ B, x \times y ∈ B$

#### Exemples

Si on travaille dans $\mathbb{C}$ :

$\mathbb{Z}, \mathbb{D}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ sont des sous-anneaux de $(\mathbb{C}, +, \times)$

- Soit $I$ un intervalle de $\mathbb{R}$
- $\mathbb{R}[x]$ 
- $x \mapsto k, k ∈ \mathbb{R}$
- $C^{n}(I, \mathbb{R})$ avec $n ∈ \mathbb{N} \cup \{\infty\}$   
- $\mathcal{D}(I, \mathbb{R})$ 

Sont des sous-anneaux de $(I^{\mathbb{R}}, +, \times)$ 

### Quelques regles de calcul dans les anneaux

On considère $(A, +, \times)$ un anneau

#### Propriété

$$
∀ a ∈ A, a \times 0_A = 0_A \times a = 0_A
$$

#### Preuve
$$
a \times 0_A = a \times \overbrace{(0_A + 0_A)}^{0_A \text{ est neutre de + }} = a \times 0_A + a \times 0_A \\
\underbrace{a \times 0_A = 0_A}_{\text{car } 0_A \times a \text{ est inversible par } +}
$$

#### Remarque

La reciproque est fausse:

$$
∀ a, b ∈ A, (a \times b = 0) \implies a = 0 \text{ ou } b = 0
$$

Cela est faux en général

Si c'est le cas on dit que l'anneau est **intègre**.

#### Exemple
- $(\mathbb{C}, +, \times)$ est intègre
- $(\mathbb{R}^{\mathbb{R}}, + \times)$ ne l'est pas car $\mathbb{1}_{\mathbb{Q}} \times \mathbb{1}_{\mathbb{R}} = 0$

#### Théorème "Formule du Binome de Newton"

Soient $a, b, ∈ A, n ∈ \mathbb{N}$

Si $a \times b = b \times a$ alors

$$
(a+b)^{n} = \sum_{k=0}^{n} \binom{n}{k} a ^{k} b ^{n-k}
$$

#### Remarque

$$
(a+b)^2 = a^2 + 2ab + b^2 \iff (a+b)^2 = a^2+ ab + ba + b^2
$$

Ainsi il faut que: $2ab = ab + ba$ 

#### Théorème "Troisième Identité Remaruqable généralisée"

Soient $a, b ∈ A$ et $n ∈ \mathbb{N}^{*}$ alors:

$a^{n} - b^{n} = \sum_{k=0}^{n} a^{k}b^{n-k}$ 

### L'ensemble des inversibles d'un anneau

Soit $(A, +, \times)$ un anneau

On note $A^{*}$ l'ensemble des inversibles de $A$ pour la loi $\times$.

Ainsi $A^{*} = \{ a ∈ A / ∃ b ∈A / a \times b = b \times a = 1_A\}$ 

#### Théorème

Si $(A, +, \times)$ est un anneau alors $(A^{*}, \times)$ est un groupe

Si $(A, +, \times)$ est commutatif alors $(A^{*}, \times)$ est abélien.  

#### Preuve

- Si $a, b ∈ A^{*}$ alors $a \times b ∈ A^{*}$ Donc $\times$ est une loi de composition interne sur $A^{*}$.
- $∀ a ∈ A^{*}, 1_A \times a = a \times 1_A = a$, $1_A \times 1_A = 1_A ∈ A^{*}$ donc $(A^{*}, \times)$ possède l'élément neutre $1_A$
- $∀ a ∈ A^{*}, a \times a^{-1} = a^{-1} \times a = 1_A$ donc $a^{-1} ∈ A^{*}$
- $\times$ est associative sur $A$ donc sur $A^{*}$
- Si $\times$ commutative sur $A$ alors elle l'est sur $A^{*}$        

#### Exemples

- $\mathbb{C}^{*} = \mathbb{C} \backslash \{0\}$
- $\mathbb{R}^{*} = \mathbb{R} \backslash \{0\}$  
- $\mathbb{Q}^{*} = \mathbb{Q} \backslash \{0\}$  
- $\mathbb{Z}^{*} = \{ \pm 1\}$ 
- $C^{0}([0,1], \mathbb{R})^{*} = \{ f ∈ C^{0}([0,1], \mathbb{R}) / ∀ x ∈ [0,1], f(x) \neq 0 \}$ 

### Morphismes d'anneaux

Soient $(A, +, \times)$ et $(B, +, \times)$  (ici les $+$ et $\times$ des deux anneaux ne sont pas nécéssairement les mêmes  )

#### Définition *Morphisme d'anneau*

On dit que $φ :A \to B$ est un morphisme d'anneau si

- $∀ a, b ∈ A, φ (a + b) = φ (a) + φ (b)$
- $∀ a, b ∈ A,  φ (a \times b) = φ (a) \times φ (b)$   

#### Exemples
- $\text{Id}$ et $z \mapsto \overline{z}$ de $(\mathbb{C}, +, \times)$ dans $(\mathbb{C}, +, \times)$ 
- $φ : C^{0}([0,1], \mathbb{C}) \to \mathbb{C}, f \mapsto f(0)$ est un morphisme d'anneaux de $(C^{0}([0,1], \mathbb{C}), +, \times)$ dans $(\mathbb{C}, +, \times)$  

#### Remarque
- $φ (1_A) = 1_B$ n'est pas automatique
- un morphisme d'anneaux en est un de groupes
- En particulier $φ (0_A) = 0_B$  
- $∀ a, b ∈ A, φ (a - b) = φ (a) - φ (b)$
- $∀a ∈ A^{*}, φ (a) ∈ B^{*}$ et $φ (a) ^{-1} = φ (a^{-1})$   

On peut definir le noyau et l'image d'un morphisme d'anneau 

et $\text{Ker}( φ )$ n'est peut-être pas un sous anneau de $(B, +, \times)$  

#### Théorème

Soit $φ : A \to B$ un morphisme d'anneau

- Si $A'$ est un sous-anneau de $(A, +, \times)$ alors $φ (A')$ est un sous-anneau de $(B, +, \times)$
- Si $B'$ est un sous-anneau de $(B, +, \times)$ alors $φ^{-1} (B')$ est un sous-anneau de $(A, +, \times)$

#### Définition *Isomprphisme d'anneau*

$φ : A \to B$ est un isomorphisme d'anneau si $φ$ est bijectif  

## Corps

#### Définition *Corps*

On dit que $(K, +, \times)$ est un corps si

1. $(K, +, \times$ est un anneau
2. $∀ x ∈ K \backslash \{ 0_K \}, x$ est inversible pour la loi $\times$   

#### Définition *Sous-corps*

$L$ est un sous-corps de $(K, +, \times)$ si
- $L$ est un sous-anneau de $(K, +, \times)$
- $∀ x ∈ L \backslash \{0_K \}, x$ est inversible par la loi $\times$   

#### Théorème

Si $L$ est un sous-corps d'un corps $(K, +, \times)$  alors $(L, +, \times)$ est un corps

#### Exemples

- $(\mathbb{C}, +, \times), (\mathbb{R}, +, \times), (\mathbb{Q}, +, \times)$ sont des corps
- $(\mathbb{Z}, +, \times)$ n'en est pas  

Si $K$ est un corps et $A$ un enseble quelconque alors $A^{K}$ n'est pas nécéssairement un corps 

#### Remarque
- Si $(K, +, \times)$ est un anneau alors $(K, +, \times)$ est un corps si et seulement si $K^{*} = K \backslash \{ 0_K \}$   
- Si $(K, +, \times)$ est un corps contenant un nombre fini d'éléments alors il est commutatif (Théorème de Wederburn) 
- Existe-t-il un corps non commutatif, oui l'ensemble des quaternions
