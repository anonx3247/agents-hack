# Chapitre 13: Dérivabilité des fonctions a valeurs réelles ou complexes

Dans un premier temps $f$ esigneras une fonction definie sur un intervalle $I$, non vide de $\mathbb{R}$ a valeurs réelles.

## Notion de dérivabilité

### Fonction dérivable en un point

#### Définition *Dérivable en un point*

Soit $x_0 ∈ I$, On dit que $f$ est derivable en $x_0$ si:
$$
\lim_{x\to x_0,x \neq x_0} \frac{f(x) - f(x_0)}{x - x_0}
$$    

existe et est finie.

Dans ce cas la limite se note: $f'(x_0)$ et on a
$$
f'(x_0) = \lim_{h\to 0} \frac{f(x_0 + h) - f(x)}{h}
$$ 

#### Propriété

Si $f$ est derivable en $x_0$ alors $f$ est continue en $x_0$. La reciproque est fausse.

#### Preuve 
Pour $x \neq x_0$,

$$
f(x) - f(x_0) = \left(\frac{f(x) - f(x_0)}{x - x_0}\right) \times (x - x_0) \to_{x\to x_0} f'(x_0) \times 0
$$

Donc
$$
\lim_{x\to x_0, x \neq x_0} f(x) = f(x_0)
$$

Donc $f$ est continue en $x_0$

#### Contre-exemples pour la reciproque
$$
x \mapsto |x|, x \mapsto \sqrt{x}
$$
Continues mais non-dérivables en 0.

### Dérivée a gauche ou a droite

#### Définition *Dérivée a droite/a gauche*

Soit $x_0 ∈ I$, 

On dit que $f$ est dérivable en $x_0$ a gauche si
  
$$
\lim_{x\to x_0,x < x_0} \frac{f(x) - f(x_0)}{x - x_0}
$$    

existe et est finie.

On note $f'_g(x_0)$ 

On dit que $f$ est dérivable en $x_0$ a droite si
  
$$
\lim_{x\to x_0,x > x_0} \frac{f(x) - f(x_0)}{x - x_0}
$$    

existe et est finie.

On note $f'_d(x_0)$ 

#### Exemple
Pour $x \mapsto |x|$, on a:
$$
f'_g(0) = -1, f'_d(0) = 1
$$ 

#### Théorème
On dit que $f$ est dérivable en $x_0 ∈ I$ si et seulement si $f'_g(x_0) = f'_d(x_0)$

#### Preuve

" $\implies$ " :
$$
f'(x_0) = \lim_{x\to x_0, x \neq x_0} \frac{f(x) - f(x_0)}{x - x_0}
$$ 
Donc
$$
f'(x_0) = f'_g(x_0) = \lim_{x\to x_0, x < x_0} \frac{f(x) - f(x_0)}{x - x_0}
$$

$$
f'(x_0) = f'_d(x_0) = \lim_{x\to x_0, x > x_0} \frac{f(x) - f(x_0)}{x - x_0}
$$

" $\impliedby$ " :

$l = f'_g(x_0) = f'_d(x_0)$

Donc
$$
l = f'_g(x_0) = \lim_{x\to x_0, x < x_0} \frac{f(x) - f(x_0)}{x - x_0}
$$

$$
l = f'_d(x_0) = \lim_{x\to x_0, x > x_0} \frac{f(x) - f(x_0)}{x - x_0}
$$

$$
l = f'(x_0) = \lim_{x\to x_0, x \neq x_0} \frac{f(x) - f(x_0)}{x - x_0}
$$

### Opérations sur les fonctions dérivables

#### Théorème
Soient $f, g: I \to \mathbb{R}, x_0 ∈ I$.

On supoose que $f,g$ dérivables en $x_0$ alors $f+g$ et $f \times g$ sont aussi dérivables en $x_0$

Somme
$$
\frac{(f+g)(x_0 + h) - (f+g)(x_0)}{h} 
$$     
$$
\frac{f(x_0 + h) + g(x_0 + h) - f(x_0) - g(x_0)}{h} 
$$     
$$
\frac{f(x_0 + h) - f(x_0) +}{h}  + \frac{ g(x_0 + h) - g(x_0)}{h}
$$     
$$
\lim_{h\to 0} \frac{f(x_0 + h) - f(x_0) +}{h}  + \frac{ g(x_0 + h) - g(x_0)}{h} = f'(x_0) + g'(x_0)
$$
Produit
$$
\frac{(f \times g)(x_0+h) - (f \times g)(x_0)}{h}
$$
$$
\frac{f(x_0 + h) \times g(x_0 + h) - f(x_0) \times g(x_0)}{h}
$$
$$
\frac{(f(x_0 + h)  - f(x_0) )\times g(x_0 + h) - f(x_0) \times (g(x_0) - g(x_0 + h))}{h}
$$
$$
\frac{(f(x_0 + h)  - f(x_0) )\times g(x_0 + h) + f(x_0) \times (g(x_0+h) - g(x_0))}{h}
$$
$$
\frac{f(x_0+h) - f(x_0)}{h} \times g(x_0 + h) + f(x_0) \times \frac{g(x_0+h) - g(x_0)}{h}
$$
$$
\lim_{h\to 0} \frac{f(x_0+h) - f(x_0)}{h} \times g(x_0 + h) + f(x_0) \times \frac{g(x_0+h) - g(x_0)}{h} \\ = f'(x_0)g(x_0) + f(x_0)g'(x_0)
$$

#### Théorème
$f(x_0) \neq 0$
alors $(\frac{1}{f})$ est dérivable en $x_0$ et $(\frac{1}{f})'(x_0) = \frac{-f'(x_0)}{f(x_0)^2}$

#### Corollaire
$f,g : I \to \mathbb{R}$ derivables.

si $g(x_0) \neq 0$ alors $(\frac{f}{g})(x_0)$ est derivable et $(\frac{f}{g})'(x_0) = \frac{f'(x_0)g(x_0) - f(x_0)g'(x_0)}{g^2(x_0)}$

#### Théorème
Soit $x_0, λ ∈ \mathbb{R}$
$$
∃ f'(x_0) \implies ∃ (λ f)'(x_0) = λ \times f'(x_0)
$$ 

#### Théorème
On suppose que $f : I \to \mathbb{R}$ et $g : J \to \mathbb{R}$ avec $f(I) ⊂ J$. Soit $x_0 ∈ I$.

Si $f$ derivable en $x_0$ et $g$ derivable en $f(x_0)$ alors la composée $g \circ f (x_0)$ est dérivable en $x_0$
et
$$
(g \circ f)'(x_0) = g' \circ f(x_0) \times f'(x_0)
$$
$$
\lim_{h\to 0} \frac{g(f(x_0 + h)) - g(f(x_0))}{h}
$$
$$
\lim_{h\to 0} \frac{g(f(x_0 + h)) - g(f(x_0))}{f(x_0+h) - f(x_0)} \times \frac{f(x_0+h) - f(x_0)}{h}
$$
On pose $k = f(x_0 + h) - f(x_0)$ 
$$
\lim_{h\to 0} \frac{g(f(x_0 + h)) - g(f(x_0))}{k} \times \frac{k}{h}
$$

or $k \to 0$ donc

$$
\lim_{h\to 0} g'(f(x_0)) \times \frac{k}{h}
$$
$$
g'(f(x_0)) \times \lim_{h\to 0} \frac{f(x_0 + h) - f(x_0)}{h}
$$
$$
= g'(f(x_0)) \times f'(x_0)
$$

##### Démonstration 2

On pose $τ : J \to \mathbb{R}$ avec
$$
τ :y \mapsto \begin{cases}
\frac{g(y) - g(f(x_0))}{y - f(x_0)} \text{ si } y \neq f(x_0) \\
g'(f(x_0)) \text{ si } y = f(x_0)
\end{cases}
$$ 

De sorte a ce que:
$$
\lim_{h\to 0} \frac{g(f(x_0 + h)) - g(f(x_0))}{h} = 
$$
$$
τ (f(x_0 + h)) \times \overbrace{\frac{f(x_0+h) - f(x_0)}{h}}^{\text{taux d'acroissement de } f}
$$

Comme $g$ est dérivable en $f(x_0)$ on a
$$
\lim_{y\to f(x_0), y \neq f(x_0)} τ (y) = g'(f(x_0))
$$

or $g'(f(x_0)) = τ (f(x_0))$

Donc
$$
\lim_{y \to f(x_0)} τ (y) = g'(f(x_0))
$$
(Sans que la condition $y \neq 0$ ne soit requise)

Par composition de limites, 
$$
\lim_{h\to 0, h \neq 0}τ (f(x_0+h)) = g'(f(x_0))
$$
FInalement,
$$
\lim_{h\to 0, h \neq 0} \frac{g \circ f (x_0 + h) - g \circ f (x_0)}{h} = g'(f(x_0)) \times f'(x_0)
$$

### Fonction dérivable sur un intervalle

#### Définition

$f$ est dérivable sur $J ⊂ I$ si elle est dérivable sur tout point de $J$.

## Théorème de Rolle / Théorème des accroissements finis

### Conditions nécessaires d'existence d'un extremum local en un point interieur

#### Définition *Extremum local*
Soit $f: I \to \mathbb{R}, a ∈ I$

On dit que $f$ admet un maximum local si $∃ δ > 0 / ∀ x ∈ I, (|x-a| \le δ \implies f(x) \le f(a)$ 


On dit que $f$ admet un minimum local si $∃ δ > 0 / ∀ x ∈ I, (|x-a| \le δ \implies f(x) \ge f(a)$ 

On dit que $f$ admet un extremum local si elle admet un maximum ou un minimum local

#### Exemple
la fonction $x \mapsto x^{4}$
la fonction:
$$
f: [1,10] \to \mathbb{R}\\ x \mapsto \begin{cases}
2 \text{ si } x = 1 \\
x \text{ si } x \neq 1
\end{cases}
$$ 

deux maximums locaux: en 1 et en 10. Celui en 10 est global.

#### Théorème

Soit $f: I \to \mathbb{R}, x_0 ∈ I^{o}$

On suppose que $f$ est dérivable en $x_0$.

Si $f$ admet un extremum local en $x_0$ alors $f'(x_0) = 0$

#### Preuve

On peut facilement remplacer $f$ par $-f$ donc on traiteras que le cas d'un maximum.

$$
∃ δ > 0 / ∀ x ∈ I, (|x- x_0| \le δ \implies f(x) \le f(x_0))
$$

Comme $x_0 ∈ I^{o}$, $∃ δ ' >0 / [x_0 - δ ', x_0 + δ '] ⊂ I$

Soit $δ '' = \text{min}(δ , δ ')$ 
Soit $x ∈ \mathbb{R} / |x-x_0| \le δ ''$
d'une part $|x - x_0| \le δ '$ donc $x ∈ I$, d'autre part $|x-x_0| \le δ $ donc $f(x) \le f(x_0)$

Donc $∀ x ∈ [x_0 - δ '', x_0 + δ ''], f(x) \le f(x_0)$

or $∀ x ∈ [x_0 - δ '', x_0[, \frac{f(x)- f(x_0)}{x - x_0} \ge 0$
En faisant tendre $x\to x_0$ on obtient $f'_g(x_0) \ge 0$

or $∀ x ∈ ]x_0, x_0+ δ ''], \frac{f(x)- f(x_0)}{x - x_0} \le 0$
En faisant tendre $x\to x_0$ on obtient $f'_d(x_0) \le 0$

Par égalité des dérivées a droite et a gauche, et par double inégalité on a $f'(x_0) = 0$.


#### Remarque

Ce théorème est faux si $x_0$ est une borne de $I$.
La réciproque du théorème est aussi fausse.  

### Théorème de Rolle / Égalité des acroissements finis

#### Théorème "Théorème de Rolle"

Soit $f : [a,b] \to \mathbb{R}$
avec $[a,b]$ un segment de $\mathbb{R}$.
Si $f ∈ (C^{0}, [a,b])$ dérivable sur $]a,b[$ et si $f(a) = f(b)$ alors $∃ c ∈ ]a,b[ / f'(c) = 0$

#### Preuve

$f ∈ (C^{0}, [a,b])$ donc elle possede un maximum et un minimum $M,m$ respectivement.

**Cas 1**: Si $m = M$ donc $∀ x ∈ [a,b] , f(x) = m = M \text{ et } f'(x) = 0$ Donc n'importe quel $c ∈ ]a,b[$ convient.

**Cas 2**:Cas ou $M > m$
Il existe alors $x_0 ∈ [a,b] / M = f(x_0)$

**Sous-Cas 2.1**: Si $x_0 ∈ ]a,b[$ alors $f'(x_0) = 0$ et $c = x_0$ convient   

**Sous-Cas 2.2**: Si $x_0 = a \text{ ou } x_0 = b$ alors Si $x_1 = a \text{ ou } x_1 = b$ alors $f(x_1) = f(a) \text{ ou } f(x_1) = f(b)$  or $f(a) = f(b) \implies m = M$ or $M > m$ donc ce cas est impossible.

donc on se ramene au cas precedent.

#### Remarque

Le théorème est mis en defaut si on omet une des 3 hypothèses. 

Par exemple $f: [0,1] \to \mathbb{R}, x \mapsto x$. $f(0) \neq f(1)$ et $f'(x)$ ne s'anulle pas.

Par exemple $f: [0,1] \to \mathbb{R}, f ∉ (C^{0}, [0,1])$ alors $f(0) = f(1)$ mais $f'(x)$ ne s'anulle pas sur $]0,1[$.

Par exemple si $f$ est non dérivable, alors $f'(x)$ ne s'anulle pas car elle n'existe pas.

#### Théorème "l'égalité des acroissements finis"

Si $f ∈ (C^{0}, [a,b])$ et $f$  dérivable sur $]a,b[$ alors $∃ c ∈ ]a,b[ / \frac{f(b) - f(a)}{b-a} = f'(c)$

## Inégalité des acroissements finis

#### Théorème "Inégalité des acroissements finis"

Soit $f: [a,b] \to \mathbb{R}$ une fonction.

On suppose que
- $f$ est continue sur $[a,b]$
- $f$ est dérivable sur $]a,b[$
- $f'$ est borné sur $]a,b[$

Alors
$$
|f(b) - f(a)| \le \text{sup}_{x ∈ ]a,b[} |f'(x)| \times |b-a|
$$ 

En particulier, si $∀ x ∈ ]a,b[, |f'(x) \le M$ alors $|f(b) - f(a)| \le M \times |b - a|$

#### Preuve

On pose $A = \{ |f'(x)| / x ∈ ]a,b[ \}$ 
- $A$  est une partie de $\mathbb{R}$ 
- $A \neq \varnothing$ car $|f'(a+b)/2| ∈ A$
- $A$ est majoré car $f'$ est bornée

Donc $A$ possède une borne supérieure notée:
$$
\text{sup}_{x ∈ ]a,b[} |f'(x)|
$$ 

D'après l'égalité des acroissements finis:
$$
∃ c ∈ ]a,b[ / \frac{f(b)- f(a)}{b - a} = f'(c)
$$

Donc $|f(b) - f(a)| = |f'(c)| \times |b-a| \le \text{sup}_{x ∈ ]a,b[} |f'(x) \times |b-a|$ 

#### Exercice: Montrer que
$$
∀ a,b ∈ \mathbb{R}, |\sin(b) - \sin(a)| \le |b-a|
$$

#### Définition *Fonction Lipschitzienne*

Soit $f: I \to \mathbb{R}$, $f$ est lipschitzienne si :
$$
∃ K ∈ \mathbb{R} / ∀ x, y ∈ I, |f(x) - f(y)| \le K|x-y|
$$

#### Exemple
la fonction $|x|$, est lipschitzienne de constante $K=1$ donc elle est
>"1-lipschitzienne" 

(D'après l'inégalité triangulaire)

#### Théorème

Si $f$ est lipschitzienne, alors $f$ est continue.

#### Preuve
On suppose que $f$ est lipschitzienne
Donc $∃ K ∈ \mathbb{R} / ∀ x,y ∈ I, |f(x) - f(y)| \le K |x-y|$

Soit $x_0 ∈ I$ montrons que $f$ est continue en $x_0$.
$∀ x ∈ I, |f(x) - f(x_0)| \le K |x-x_0|$

Comme $\lim_{x\to x_0} |x-x_0| = 0$, par encadrement, la limite quand $x\to x_0$ de $f(x)$ existe et vaut $f(x_0)$.

Ceci est vrai pour tout $x_0 ∈ I$ donc $f$ est continue sur $I$.

#### Remarque
La reciproque est fausse, par exemple:
$$
f: x \mapsto \sqrt{x} \\
f ∈ (C^{0}, \mathbb{R}^{+})
$$

Mais elle n'est pas lipschitzienne sur $\mathbb{R}^{+}$.

#### Remarque

En revanche $x \mapsto \sqrt{x}$ est lipschitzienne sur tout intervalle de la forme $[ε, + \infty[$ avec $ε > 0$

#### Théorème: " Caractérisation des fonctions lipschitziennes parmi les fonctions dérivables"
Soit $I \to \mathbb{R}$ une fonction dérivable.

$f$ est lipschitzienne $\iff$ $f'$ est bornée.

#### Preuve

"$\impliedby$": $∃ M ∈ \mathbb{R} / ∀ t ∈ I,|f'(t)| \le M$

Soient $s, y ∈ I$

$f ∈ (C^{1}, [x,y])$, De plus $f'$ est bornée sur $]x,y[$ donc par inégalité des accroissements finis, on a:
$$
|f(x) - f(y)| \le M |x-y|
$$    
Donc $f$ est lipschitzienne.

"$\implies$ ": $∃ K ∈ \mathbb{R} / ∀ x,y ∈ I, |f(x) - f(y)| \le K|x-y|$
Donc
$$
∀ x \neq y ∈ I, \lvert\frac{f(x) - f(y)}{x - y} \rvert
$$ 

en passant a la limite avec $y\to x , x \neq y$ on obtient:
$$
|f'(x)| \le K
$$ 
Donc $f'$ est bornée. 

## Régularité d'une fonction

### Fonction de classe $C^{n}$ avec $n ∈ \mathbb{N} \cup \{\infty\}$  

#### Définition *Classe $C^{0}$*
- On dit que $f$ est de classe $C^{0}$ sur $I$ si elle est continue sur $I$. On note $f ∈ C^{0}(I, \mathbb{R})$.
- On dit que $f$ est de classe $C^{n}$ sur $I$ si elle est continue et dérivable $n$ fois. on note $f ∈ C^{n}(I, \mathbb{R})$
- On dit que $f$ est de classe $C^{\infty}$ si $f$ est infiniment dérivable. On note $f ∈ C^{\infty}(I, \mathbb{R})$ 

#### Remarque:
$$
\bigcap_{n ∈ \mathbb{N}} C^{n}(I, \mathbb{R}) = C^{\infty}(I, \mathbb{R}).
$$

Si on note $\mathcal{D}(I, \mathbb{R})$ l'ensemble des fonctions dérivables sur $I$ alors.

#### Exemple
Soit $α ∈ \mathbb{R}, x \mapsto e^{α x} ∈ C^{\infty}(\mathbb{R})$ et $∀ n ∈ \mathbb{N}$

$$
\frac{d^{n}}{dx^{n}} e^{α x} = α ^{n} e^{α x}
$$

Soit $p ∈ \mathbb{N}, x \mapsto x^{p} ∈ C^{\infty}(\mathbb{R})$, avec
$$
\frac{d^{n}}{dx^{n}} x^{p} = n! \binom{p}{n} x^{p-n}
$$

### Le théorème de la limite de la dérivée

#### Théorème "Le théorème de la limite de la dérivée"

Soit $f: I \to \mathbb{R}$ et $a ∈ I$.

On suppose
- $f ∈ C^{0}(I, \mathbb{R})$
- $f$ dérivable sur $I\backslash \{a\}$
- $∃ l ∈ \mathbb{R} / \lim_{x \to a, x \neq a} f'(x) = l$ 

ALors $f$ est dérivable en $a$ et $f'(a) = l$.   

#### Preuve

Soit $x ∈ I \backslash \{a\}$

$f$ est continue sur $[a,x]$ et $f$ est dérivable sur $]a,x[$ donc d'après l'égalité des acroissements finis:

$$
∃ c_x∈ ]a, x[ / \frac{f(x) - f(a)}{x - a} = f'(c_x)
$$

On a donc l'existence(-) d'une fonction:

$$
c : x \mapsto c_x
$$

Avec $c  : I \backslash \{a\} \to \mathbb{R}$
verifiant $∀ x ∈ I \backslash \{a\}, c(x) ∈ ]a,x[$
et 
$$
∀ x ∈ I \backslash \{a\}, \frac{f(x) - f(a)}{x - a} = f'(x)
$$   

Par encadrement (car $c(x) ∈ ]a,x[$ )
$$
\lim_{x \to a, x \neq a} c(x) = a
$$
Donc
$$
\lim_{x \to a, x \neq a} f'(c(x)) = l
$$
Par composition de limites.

$f$ est donc dérivable en $a$ et $f'(a) = l$.

#### Remarque

Pour le faire on utilise l'axiome du choix (qui est rejeté par certains).

### Opérations sur les fonctions de classe $C^{n}$

#### Théorème
Si $f$ et $g$ sont de classe $C^{n}$ sur $I$, alors $f+g$ est de classe $C^{n}$ sur I et $(f+g)^{(n)} = f^{(n)} + g^{(n)}$  

#### Théorème
Si $f$ est de classe $C^{n}$ sur $I$, et $λ ∈ \mathbb{R}$ alors $λ f$ est de classe $C^{n}$ sur I et $(λ f)^{(n)} = λ f^{(n)}$

#### Théorème
Si $f$ et $g$ sont de classe $C^{n}$ sur $I$ et $g$ ne s'anulle pas dans $I$ alors $\frac{f}{g}$ est de classe $C^{n}$ sur $I$.         

#### Théorème
Si $f$ et $g$ sont de classe $C^{n}$ sur $I$, alors $f\times g$ est de classe $C^{n}$ sur I et
$$
(f \times g)^{(n)} = \sum_{k=0}^{n} \binom{n}{k} f^{(k)}g^{(n-k)}
$$


## Complement au Theoreme de la Bijection

#### Théorème

Soit $f$ une fonction continue et strictement monotone sur $I$.

SOit $x_0 ∈ I$ On suppose que $f$ est derivable en $x_0$ On pose $y_0 = f(x_0)$

$f^{-1}$ est derivable en $y_0$ si et seulement si $f'(x_0) \neq 0$.
Dans ce cas, $(f^{-1})'(y_0) = \frac{1}{f' \circ f^{-1} (y_0)} = \frac{1}{f'(x_0)}$

#### Preuve

On pose $φ : I \to \mathbb{R}$
$$
x \mapsto \begin{cases}
\frac{f(x) - f(x_0)}{x - x_0} \text{ si } x \neq x_0 \\
f'(x_0) \text{ sinon}
\end{cases}
$$

comme $f$ derivable en $x_0$ alors $\lim_{x\to x_0, x \neq x_0} φ (x) = φ (x_0)$ 

De plus $f^{-1}$ est continue en $y_0$ Donc $\lim_{y \to y_0} f^{-1}(y) = ^{-1}(y_0) = x_0$

Donc par composition de limites

$$
\lim_{y\to y_0} φ \circ f^{-1}(y) = φ (x_0) = f'(x_0)
$$

En particulier quand $y \neq y_0$ 
$$
\lim_{y \to y_0, y \neq y_0} φ \circ f^{-1}(y) = \lim_{y\to y_0, y \neq y_0} \frac{f \circ f^{-1} (y) - f(x_0)}{f^{-1} (y) - x_0} \\
= \lim_{y \to y_0, y \neq y_0} \frac{y - y_0}{f^{-1}(y) - f^{-1}(y_0)}
$$

On suppose que $f'(x_0) \neq 0$ Alors  par inverse on a
$$
\lim_{y\to y_0, y \neq y_0} \frac{f^{-1}(y) - f^{-1}(y_0)}{y - y_0} = (f^{-1})' (y_0) = \frac{1}{f'(x_0)}
$$  

On suppose $f^{-1}$ derivable en $y_0$  
$$
\lim_{y\to y_0, y \neq y_0} \frac{f^{-1}(y) - f^{-1}(y_0)}{y - y_0} = (f^{-1})' (y_0) = \frac{1}{f'(x_0)} \implies f'(x_0) \neq 0
$$  


#### Corollaire

On suppose que $f$ est strictement monotone sur un intervalle $I$

- Si $f$ est derivable sur $I$ et si $f'$ ne s'anulle pas sur $I$  alors  $f^{-1}$ est derivable sur $J = f(I).$

- Pour $n ∈ \mathbb{N}^{*} \cup \{ \infty \}$ si $f$ est de classe $C^{n}$, $f^{-1}$ est de classe $C^{n}$ sur $J$ 

- Si $x_0 ∈ I$ on pose $y_0 = f(x_0)$. Si $f$ est continue sur $I$ et si $f$ derivable en $x_0$ et si $f'(x_0) = 0$ alors $\mathcal{C}_{f^{-1}}$ admet au point d'abscisse $y_0$ une tangent verticale.


#### Définition 

Soit $f:I \to \mathbb{C}$ et $a ∈ I$

On dit que $f$ est derivable en $a$ si $\Re(f)$ et $\Im(f)$ sont derivables en $a$.

Dans ce cas $f'(a) = \Re(f)'(a) + i \Im(f)'(a)$ 

#### Remarque

$\Re(f'(a)) = \Re(f)'(a)$  et $\Im(f'(a)) = \Im(f)'(a)$

#### Exemples

- Si $a ∈ \mathbb{C}$ alors $f: x \mapsto e^{ax}$ est derivable sur $\mathbb{R}$ et $f': x\mapsto ae^{ax}$

- Si $a ∈ \mathbb{C}$ et $n ∈ \mathbb{N}$, $f: x \mapsto (x+a)^{n}$ est derivable sur $\mathbb{R}$ et $f':x \mapsto n(x+a)^{n-1}$      

**Quels sont les theoremes vus pour les fonctions a valeurs reelles, qui restent valident pour les fonctions a valeurs complexes?**

- Les operations sont valides et dans la composition, la fonction interieure doit etre a valeurs reelles.
- Le theoreme sans nom mais **hyper**-*important* portant sur les extremums locaux n'est plus valide car son enonce n'a plus de sens (il n'existe pas de relations d'ordre dans $\mathbb{C}$).
- Le theoreme de Rolle et l'egalite des acroissements finis ne sont plus valides pour les fonctions a valeurs complexes.
#### Exemple

Soit $f x \mapsto e^{ix}$ sur $[0,2 π ]$

$f$ est continue sur $[0, 2 π ]$ et derivable sur $]0, 2 π [$ et $f(0) = f(2 π )$

Or $f'$ ne s'anulle jamais car $∀ x ∈ [0, 2 π ], |f'(x)| = |ie^{ix}| = 1$  


- Le theoreme de la limite de la derivee et l'inegalite des acroissements finis sont valides pour les fonctions a valeurs complexes, malgre la necessite d'utilier le theoreme de Rolle qui lui n'est pas valide.

    - Pour prouver le theoreme de la limite de la derivee complexe on applique separement a la partie reelle et la partie imaginaire le theoreme de la limite de la derivee reelle
    - L'inegalite des acroissements finis:
    On suppose donne une fonction $f: [a,b] \to \mathbb{C}$ qui verifie $f ∈ C^{0}([a,b])$ et $f ∈ C^{1}(]a,b[)$ et $f'$ est bornee sur $]a,b[$.
    Alors $|f(b) - f(a)| \le \text{sup}_{t ∈ ]a,b[ } |f'(t)| \times |b - a|$.

    En faisant ceci pour $\Re(f)$ et $\Im(f)$ on a:
    $$
    |f(b) - f(a)|^2 \le \text{sup} \left(|\Re(f')(t)|^2\right) + \text{sup} \left(|\Im(f')(t)|^2\right) \times |b - a|
    $$
    Ce qui ne convient pas. 
    
    Or on peut le faire comme suit:
    on pose $g: [a,b] \to \mathbb{R}$
    $$
    x \mapsto \Re( (f(x) - f(a)) \times (\overline{f(b) - f(a)}))
    $$ 

    $g$ est continue sur $[a,b]$ car $f$ l'est, elle est derivable sur $]a,b[$ car $f$ l'est.

    $∀ x ∈ ]a,b[, |g'(x)| = |\Re(f'(x) \times (\overline{f(b) - f(a)})| \le | f'(x) \times (\overline{f(b)- f(a)}| = |f'(x)| \times |\overline{f(b) - f(a)}| \le \text{sup} |f'(x)| \times |f(b)-f(a)|$

    D'apres le l'inegalite des acroissements finis appliques a $g$ on obtient:

    $$
    |g(b) - g(a)| \le \text{sup} |f'(x)| \times |f(b) - f(a)| \times |b-a|
    $$ 

    Or $g(a) = 0$ et $g(b) = |f(b) - f(a)|^2$

    Donc
    $$
    |f(b) - f(a)|^2 \le \text{sup} |f'(x)| \times |f(b) - f(a)| \times |b-a|
    $$ 
    
    Si $f(a) = f(b)$ l'inegalite est bannale.
    Sinon $|f(b) - f(a)| \neq 0$ alors en simplifiant, on trouve
    $$
    |f(b) - f(a)| \le \text{sup} |f'(x)| \times |b-a|
    $$  