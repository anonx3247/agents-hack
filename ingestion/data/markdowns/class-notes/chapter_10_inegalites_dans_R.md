# Chapitre 10: Inegalites dans R

Dans ce chapitre, on etudie la relation d'ordre usuelle de $\mathbb{R}$.



## Borne superieure, borne inferieure

### Definition et exemples

#### Définition *borne superieure/inferieure*

Soit $A$ un ensemble de $\mathbb{R}$, on appelle borne superieure de $A$, si elle existe, le plus petit des majorants de $A$. Elle se note $\sup(A)$ .        

Soit $A$ un ensemble de $\mathbb{R}$, on appelle borne inferieure de $A$, si elle existe, le plus grand des minorants de $A$. Elle se note $\inf(A)$ .

#### Exemples

- $A = [0,1]$, $\sup(A) = 1, \inf(A) = 0$
- $A = ]0,1[, \sup(A) = 1, \inf(A) = 0$
- $A = ]0,+\infty[, \inf(A) = 0, \nexists \sup(A)$ 

#### Remarque

- En general, $\sup(A) ∉ A$
- $\inf(A) ∉ A$.
- En admettat une borne superieure, si et seulement si $A$ admet une borne inferieure:

$$
\inf(-A) = -\sup(A)
$$

### Un theoreme interessant

#### Théorème

Soit $A ⊂ \mathbb{R}$

- Si $A \neq \varnothing \land ∃ M ∈ \mathbb{R} / ∀ x ∈ A, x < M \implies ∃ \sup(A)$
- Si $A \neq \varnothing \land ∃ m ∈ \mathbb{R} / ∀ x ∈ A, x > m \implies ∃ \inf(A)$

#### Preuve

Le second point se demontre a pratir du premier point, et de la remarque precedente.

On admet le premier point.

#### Corollaire

1. Si $A$ possede un maximum alors $A$ possede une borne superieure  (reciproque fausse) et $\sup(A) = \max(A)$

2. Si $A$ possede un minimum alors $A$ possede une borne inferieure (reciproque fausse) et $\inf(A) = \min(A)$

#### Preuve

Montrons (1)

1. $\max(A) ∈ A$ donc $A \neq \varnothing$, 

2. $\max(A)$ est une majorant de $A$.

3. Donc $A$ possede une borne superieure. 
3. $\max(A) ∈ A$ alors $\max(A) \le \sup(A)$.
3. or $\max(A)$ est majorant de $A$ donc $\max(A) \ge \sup(A)$.
3. Donc $\max(A) = \sup(A)$ par double inegalite.

#### Remarque

Si $A$ possede une borne superieure (respectivement une borne inferieure) alors $A$ possede un maximum (respectivement minimum) si et seulement si, $\sup(A) ∈ A$.  (respectivement $\inf(A) ∈ A$).

#### Exemple

Posons:
$$
A = \left\{ \frac{2^{n}}{2^{n}-1}, n ∈ \mathbb{N}^{*} \right\}
$$

$$
\frac{2^{n}}{2^{n}-1} = 1+\frac{1}{2^{n}-1}
$$

or on a:
$$
0 \le \frac{1}{2^{n}-1} \le 1 \iff 1 \le 1+ \frac{1}{2^{n}-1} \le 2
$$
Or $A$ est majoree donc $\sup(A)$ existe. et $A$ est minoree donc $\inf(A)$ existe.

##### Borne superieure

$$
\sup(A) \le 2
$$

​    Or $2 ∈ A \implies 2 \le \sup(A)$ donc par double inegalite on a:
$$
2 = \sup(A)
$$

 ##### Maximum

$\sup(A) ∈ A$ donc $\max(A) = \sup(A) = 2$.

##### Borne inferieure

On remarque que:
$$
∀ n ∈ \mathbb{N}^{*}, \frac{2^{n}}{2^{n}-1} ∈ A
$$
 Donc
$$
∀ n ∈ \mathbb{N}^{*}, \frac{2^{n}}{2^{n}-1} \ge \inf(A)
$$


En faisant tendre $n\to\infty$, on a:
$$
\lim_{n\to\infty} \frac{2^{n}}{2^{n}-1} = 1
$$
 On a donc:
$$
1 \ge \inf(A), \text{ or } 1 \le \inf(A) \text{ donc } 1 = \inf(A)
$$

##### Minimum

Comme $\inf(A) ∉ A$, on a pas de minimum. 

### Caracterisation des bornes superieures et inferieures

#### Théorème "Caracterisation de borne superieure"

Soit $A ⊂ \mathbb{R} / A \neq \varnothing, a ∈ \mathbb{R}$. 

$A$ admet une borne superieure et $\sup(A) = a$, si et seulement si:
$$
(∀ x ∈ A, x \le a) \land (∀ ε > 0, ∃ b ∈ A / a - ε < b)
$$

  #### Preuve

"$\implies$": 

- $∀ x ∈ A, x \le a$ car $a$ est un majorant de $A$.
- On fixe $ε>0$, et $a-ε $ n'est plus un majorant de $A$ donc $∃ b ∈ A / b > a - ε $.

"$\impliedby$":

- $A$ est non vide et $∃ a ∈ \mathbb{R} / ∀ x ∈ A, x \le a$ donc $A$ est majore.

- donc $A$ possede une borne superieure, verifiant: $\sup(A) \le a$.

- Montrons que $\sup(A) = a$ par l'absurde:

  - Supposons que $\sup(A) < a$.
  - Choisissons $ε = a - \sup(A)$.
  - Donc $a - ε = \sup(A)$, Donc

  $$
  ∃ b ∈ A / \sup(A) < b
  $$

  - On arrive donc a une absurdite, car un element de $A$ est plus grand qu'un majorant de $A$.  

#### Théorème "Caracterisation de borne inferieure"

Soit $A ⊂ \mathbb{R} / A \neq \varnothing, a ∈ \mathbb{R}$. 

$A$ admet une borne inferieure et $\inf(A) = a$, si et seulement si:
$$
(∀ x ∈ A, x \ge a) \land (∀ ε > 0, ∃ b ∈ A / a + ε > b)
$$

  #### Preuve

Voir preuve precedente.

#### Remarque

$\sup(A)$ et $\inf(A)$ sont uniques, 

## Partie entierre d'un reel

#### Théorème " $\mathbb{R}$ est archimedien"    

$$
∀y ∈ \mathbb{R}^{+*}, ∀ x ∈ \mathbb{R}, ∃ n ∈ \mathbb{N} / ny \ge x
$$

#### Preuve

On raisonne par l'absurde.

On suppose que $∃ y ∈ \mathbb{R}^{+*}, ∃ x ∈ \mathbb{R}, ∀ n ∈ \mathbb{N}, ny < x$. 

On pose $A = \{ ny / n ∈ \mathbb{N} \}$ 

1. $A ⊂ \mathbb{R}$ 
1. $A$ est majore par $x$
1. $y ∈ A$ donc $A \neq \varnothing$.

Donc $\sup(A)$ existe, notee $a$ .     
$$
∀ n ∈ \mathbb{N}, (n+1)y ∈ A
$$
Donc $∀ n ∈ \mathbb{N}, (n+1)y \le a$ 
$$
(n+1)y \le a \\
ny \le a - y
$$
On en deduit que $A$ est majore par $a-y$ est $a-y$ est plus petit que $a$, on arrive a une absurdite. 

#### Théorème

$$
∀ x ∈ \mathbb{R}, ∃ ! k ∈ \mathbb{Z} / k \le x < k+1
$$

On appelle $k$ la partie entierre de $x$, notee:
$$
\lfloor x \rfloor
$$
