# Chapitre 14: Fonctions Convexes

Dans ce chapitre $f$ designeras une fonctions definie sur un intervalle $I$ non vide de $\mathbb{R}$ a valeurs reelles.

## Definition et lien avec les cordes

#### Définition *convexite d'une fonction*

On dit que $f$ est convexe si $∀ x, y ∈ I, ∀ λ ∈ [0,1], f( λ x + (1 - λ ) y) \le λ f(x) + (1 - λ ) f(y)$

On dit que $f$ est strictement convexe si $∀ x, y ∈ I, ∀ λ ∈ ]0,1[, f( λ x + (1 - λ ) y) \le λ f(x) + (1 - λ ) f(y)$

On dit que $f$ est concave si $-f$ est convexe.  

#### Rappel

Soient $x,y ∈ \mathbb{R}, x <y$

Alors
$$
z ∈ [x,y] \iff x \le z \le y \\
\iff ∃ λ ∈ [0,1] / z ∈ λ x + (1 - λ ) y
$$


Soit $x,y ∈ I, x < y,  z ∈ [x,y]$ $f$  est convexe si $f(z) ∉ [f(x), f(y) \land f(z) \le \text{min}(f(x), f(y))$ 

#### Théorème

$f$ est convexe si et seulement si $f$ est en dessous de chacune de ses cordes.

#### Preuve

Soient $x,y ∈ I, x \neq y$ La corde relient les points $(x, f(x))$ et $(y, f(y))$.
a pour parametrage $g:z \mapsto \left( \frac{f(y) - f(x)}{y - x}\right) (z - x) + f(x)$

" $\implies$ " 
On suppose $f$ convexe. Soit $x,y ∈ I / x < y$

Montrons que la courbe representative de $\mathcal{C}_f$ est en dessous de la courbe reliant $(x, f(x))$ et $(y, f(y))$.

Soit $z ∈ [x,y]$ montrons que $f(z) \le g(z)$.

$z ∈ [x,y] \iff ∃ λ ∈ [0,1] / z = λ x + (1- λ) y$

Donc on veut que:
$$
f(z) = f( λ x + (1 - λ ) y) \le λ f(x) + (1 - λ )f(y) 
$$

or $g(z) = f(y) (1 - λ ) + λ f(x)$

" $\impliedby$ "

On suppose que $\mathcal{C}_f$ est en dessous de chacune de ses cordes, on prends $x, y ∈ I / x < y$ et $λ ∈ [0,1]$ avec $z = λ x + (1 - λ ) y$ Donc on sait que $g(z) \ge f(z)$ car
$$
f(z) = f(λ x  + (1 - λ )y) \le g(z) = λ f(x) + (1 - λ )f(y)
$$

#### Remarque

$f$ est concave si et seulement si $\mathcal{C}_f$ est au dessus de chacune de ses cordes.

$f$ est strictement convexe si et seulement si $\mathcal{C}_f$ est strictement en dessous de chacune de ses cordes.

#### Exemples

- $x \mapsto |x|$ (consequence de l'inegalite triangulaire) 
- $x \mapsto \sqrt{x}$ est concave (observation graphique)

## Caractérisation de la convexité à l'aide de la croissance des pentes

#### Théorème

$f$ est convexe si et seulement si:
$$
∀ x ∈ I, \begin{cases}

Φ _x : I \backslash \{x\} \to \mathbb{R} \\
t \mapsto \frac{f(t)- f(x)}{t - x}
\end{cases}
$$ 

est croissante.

#### Preuve

" $\impliedby$ ": Soient $x,y, ∈ I$ et $ λ ∈ [0,1]$

Montrons que $f(λ x + (1 - λ ) y) \le λ f(x) + (1 - λ ) f(y)$ (*)

(*) est vraie si $x = y$ et donc quitte a permuter $x$  et $y$ on peut supposer $x < y$

(*) est vraie si $λ ∈ \{0, 1\}$ donc on peut supposer $λ ∈ ]0,1[$

On pose $z = λ x + (1- λ ) y$ de sorte que $z ∈ ]x,y[$

On en déduit que $Φ _x (z) \le Φ _x (y)$

Donc $\frac{f(z) - f(x))}{z - x} \le \frac{f(y) - f(x)}{y - x}$

Or $z - x > 0$ donc $f(z) \le f(x) + \left(\frac{z - x}{y - x}\right) \times (f(y) - f(x))$

Or $\frac{z-x}{y-x} = \frac{λ x + (1 - λ )y}{y - x}$

$$
= \frac{-x(1 - λ ) + (1 - λ )y}{y - x} \\
= \frac{(y-x)(1 - λ )}{y - x} \\
= 1 - λ 
$$

Donc $f(z) \le f(x) + (1 - λ ) \times (f(y) - f(x)) = λ f(x) + (1 - λ)f(y)$

Donc $f$ est convexe. 


" $\implies$ " :

Soit $x ∈ I$ Montrons que $Φ _x$ est croissante.

Soient $t_1, t_2 ∈ I \backslash \{x\}$ tel que $t_1 < t_2$

Montrons que $Φ _x (t_1) \le Φ _x (t_2)$

**Cas n⁰ 1:** Cas ou $x < t_1 < t_2$

donc $t_1 ∈ [x, t_2]$

Donc $∃ λ ∈ [0,1] / t_1 = λ x + (1 - λ ) t_2$

On observe que $λ \neq 1, 0$ 
    
Comme $f$ est convexe, on a:
$$
f(t_1) \le λ f(x) + (1 - λ )f(t-2)
$$

$$
Φ _x (t_1) = \frac{f(t_1) - f(x)}{t_1 - x} \le \frac{λ f(x) + (1 - λ )f(t_2) - f(x)}{t_1 - x}
$$

$$
\le \frac{-f(x) (1 - λ ) + (1 - λ )f(t_2)}{t_1 - x}
$$

$$
\le \frac{(1 - λ )(f(t_2) - f(x))}{λ x + (1 - λ )t_2 - x}
$$

$$
\le \frac{(1 - λ )(f(t_2) - f(x))}{(1 - λ )(-x) + (1 - λ )t_2}
$$
 
$$
\le \frac{(1 - λ )(f(t_2) - f(x))}{(1 - λ )(t_2 - x)}
$$

$$
\le \frac{f(t_2) - f(x)}{t_2 - x} = Φ _x (t_2)
$$

**Cas n⁰2**: Cas ou $t_1 < t_2 < x$

Alors on a $t_2 ∈ ]t_1, x[$

et $t_2 = λ t_1 + (1 - λ ) x$

Comme $f$ est convexe, $f(t_2) \le λ f(t_1) + (1 - λ )f(x)$  

$$
f(t_1) \ge \frac{1}{λ }f(t_2) - \frac{(1- λ )}{f(x)}
$$

$$
Φ _x (t_1) = \frac{f(t_1) - f(x)}{t_1 - x} = \frac{f(x) - f(t_1)}{x - t_1}
$$

$$
\frac{f(x) - \frac{1}{λ }f(t_2) - \frac{1- λ }{(λ}f(x)}{x - t_1}
$$

$$
\frac{f(x)(1 - \frac{1 - λ }{λ }) - \frac{1}{λ }f(t_2)}{x - t_1}
$$

$$
\frac{f(x)(λ + 1 - λ ) - f(t_2)}{λ (x - t_1)}
$$

$$
\frac{f(x)- f(t_2)}{x - t_2} \text{ car } t_2 = λ (t_1 - x) + x
$$

$$
Φ _x(t_1) = Φ _x (t_2)
$$

**Cas n⁰3**: Cas ou $t_1 < x < t_2$

$x ∈ ]t_1, t_2[$ donc $∃ λ ∈ ]0,1[ / x = λ t_1 + (1 - λ ) t_2$

Comme $f$ convexe on a:

$$
f(x) \le λ f(t_1) + (1 - λ )f(t_2)
$$

$$
f(t_1) \ge \frac{f(x) - (1 - λ )f(t_2)}{λ }
$$

$$
Φ _x (t_1) = \frac{f(t_1) - f(x)}{t_1 - x} = \frac{f(x) - f(t_1)}{x - t_1}
$$
$$
\le \frac{f(x) - \frac{f(x)}{λ } + \frac{1 - λ }{λ }f(t_2)}{x - t_1}
$$
$$
\le \frac{(f(t_2) - f(x))( 1 - λ )}{λ (x - t_1)}
$$

$$
\le \frac{1 - λ }{λ } \times \frac{f(t_2) - f(x)}{x -t_1}
$$

Or $λ = \frac{x - t_2}{t_1 - t_2}$ donc $1 - λ = 1 - \frac{x - t_2}{t_1 - t_2} = \frac{t_1 - x}{t_1 - t_2}$

$$
\frac{1 - λ }{λ } = \frac{t_1 - x}{x - t_2}
$$

Donc $Φ _x (t_1) \le \frac{t_1 - x}{x- t_2} \times \frac{f(t_2) - f(x)}{x - t_1} = Φ _x (t_2)$

#### Corollaire: "Inégalité des 3 pentes"

Soit $a < b < c ∈ I$ On a

$$
\frac{f(b) - f(a)}{b - a} \le \frac{f(c) - f(a)}{c - a} \le \frac{f(c) - f(b)}{c - b}
$$

#### Preuve

$Φ _a (b) \le Φ _a(c) = Φ _c(a) \le Φ _c (b)$ 

Exercice: Établir la réciproque:

Si $f$ vérifie l'inégalité des 3 pentes, alors $f$ est convexe.  

## Caractérisation de la convexité a l'aide de la dérivée

#### Théorème
Soit $f : I \to \mathbb{R} ∈ \mathcal{D}^{1}(I, \mathbb{R})$

- $f$ est convexe si et seulement si $f'$ est croissante
- $f$ est concave si et seulement si $f'$ est décroissante     

" $\implies$ ": On suppose que $f$ est convexe.

Montrons que $f'$ est croissante.

Soit $x, y ∈ I / x \le y$ montrons que $f'(x) \le f'(y)$

1. Si $x = y$ alors l'inégalité est banale, on peut donc supposer $x < y$.

2. $∀ t ∈ ]x,y[, Φ _x(t) \le Φ _x (y)$

    Car $Φ _x$ est croissante car $f$ convexe

    Donc $∀ t ∈ ]x,y[, \frac{f(t) - f(x)}{t - x} \le \frac{f(y) - f(x)}{y - x}$

    En passant a la limite pour $t \to_{t > x} x$ on obtient

    $f'_d(x) \le \frac{f(y) - f(x)}{y - x}$

3. $∀ t ∈ ]x,y[ Φ _y (t) \ge Φ _y (x)$
    
    Car $Φ _y$ est croissante car $f$ convexe.

    Donc $∀ t ∈ ]x,y[, \frac{f(y) - f(x)}{y - x} \le \frac{f(y) - f(t)}{y - t}$

    En passant a la limite $t \to_{t < y} y$ on obtient $f'_g(y) \ge \frac{f(y) - f(x)}{y - x}$

    Donc $f'_d(x) \le \frac{f(y) - f(x)}{y - x} \le f'_g(y)$

    Or $f$ dérivable donc $f'_g = f'_d$ donc $f'(x) \le f'(y)$


" $\impliedby$ " :

On veut montrer que $f( λ x + (1 - λ ) y) \le λ f(x) + (1 - λ ) f(y)\text{  } (*)$

$(*)$ est vraie quand $x = y$ ou $λ = 0, 1$.

Quitte a permuter $x$ et $y$ on peut donc supposer $x < y$ et $λ ∈ ]0, 1[$ 

Posons:
$$
φ : [0, 1] \to \mathbb{R} \\
λ \mapsto λ f(x) + (1 - λ )f(y) - f( λ x  + (1 - λ )y)
$$

Pour prouver $(*)$ il suffit se prouver que $φ $ est positive  
$φ $ est derivable et $∀ λ ∈ [0,1]$ vaut:  

$$
φ ' ( λ ) = f(x) - f(y) + (x-y)f'(λ x + (1 - λ )y)
$$

Par l'égalité des acroissements finis,
$$
∃ c ∈ ]x, y[ / f(x) - f(y) = (x - y)f'(c)
$$

Donc $φ '( λ ) = (x - y) f'(c) - (x - y) f'( λ x + (1 - λ ) y) = (x - y)(f'(c) - f'( λ x + (1 - λ ) y))$ 

Or $c \ge λ x + (1 - λ) y \iff \frac{c-y}{x - y} \le λ $

| $λ $ | 0  | $\frac{c - y}{x - y}$ | 1 |
|------|----|-----------------------|---|
| $φ'$ |  +| 0 | - |
| $φ $ | $0 \nearrow$ | ? | $\searrow 0$ |

Donc $φ  > 0 \implies f$ est convexe. 

#### Corollaire

- $f$ est convese si et seulement si $f'' \ge 0$  
- $f$ est concave si et seulement si $f'' \le 0$

#### Exemple
$$
x \mapsto e^{x} \implies \text{ convexe sur } \mathbb{R} 
$$
$$
x \mapsto \sqrt{x} \text{ concave sur } \mathbb{R}^{+*}
$$

#### Théorème
Soit $f ∈ \mathcal{D}(I, \mathbb{R})$

$f$ est convexe si et seuelemnt si $\mathcal{C}_f$ est au dessus de chacune de ses tangentes.

#### Preuve

" $\implies$ " $x_0 ∈ I$, montrons que $\mathcal{C}_f$ est au dessur de la tangente de $\mathcal{C}_f$ au point d'abscisse $x_0$.

Cette tangente a pour équation $y = f'(x_0)(x - x_0) + f(x_0)$ 

Il s'agit de prouver que $∀ x ∈ I, f(x) \ge f'(x_0)(x - x_0) + f(x_0)$

$$
φ : I \to \mathbb{R} \\
x \mapsto f(x) - f'(x_0)(x - x_0) - f(x_0)
$$

$φ ' (x) = f'(x) - f'(x_0) \implies φ > 0$ Car $f'$ est croissante 

" $\impliedby$ " :

Soient $x, y ∈ I / x < y$

On a:
$$
∀ t ∈ I, f(t) \ge f'(x)(t - x) + f(x) \text{ } (*)
$$

$$
∀ t ∈ I, f(t) \ge f'(y)(t - y) _ f(y) \text{ } (**)
$$

En évaluant $(*)$ en $y$ on obtient:
$$
f(y) \ge f'(x)(y - x) + f(x) \iff f'(x) \le \frac{f(y) - f(x)}{y - x}
$$

En évaluant $(**)$ en $x$ on obtient:
$$
f(x) \ge f'(y)(x - y) + f(y) \iff f'(y) \ge \frac{f(y) - f(x)}{y - x} \text{ car } x - y < 0
$$

Donc $f'(x) \le \frac{f(y) - f(x)}{y - x} \le f'(y)$ 

#### Exemples
$$
x \mapsto e^{x}
$$
$\exp$ est convexe donc elle est au dessus de sa tangente en 0.

$T(x) = 1 + x$ donc $e^{x} \ge 1 +x$

$$
x \mapsto \ln x
$$

$\ln$ est concave sur $\mathbb{R}^{+*}$ donc elle est en dessous de sa tangente en 1.

## L'Inégalité de Jensen

#### Théorème "Inégalité de Jensen"

Soit $f : I \to \mathbb{R}$ convexe, soit $n ∈ \mathbb{N}^{*}$ soient, $x_1, \cdots x_n ∈ I$ et soient $λ _1 , \cdots λ _n ∈ \mathbb{R}^{+}$ tel que $∑_{k=1}^{n} λ _k = 1$ 

Alors
$$
f\left( ∑_{i=1}^{n} λ _i x _ i \right) \le ∑ _{i = 0} ^{ n} λ _i f(x_i)
$$ 


#### Remarques

- L'hypothèse implique que $∀ i ∈ [1, n], λ _i ∈ [0, 1]$
- Si $n = 2$ cette inégalité correspond a la définition de la convexité
- Généralement on applique cette inégalité lorsque tous les $λ _i$ sont égaux i.e. $λ _1 = \cdots λ _n = \frac{1}{n}$. 

#### Exemple

Soient $n ∈ \mathbb{N}, x_1, \cdots, x_ n > 0$

$\ln$ est concave sur $R^{+*}$ donc par l'inégalité de jensen on a:

$$
\ln \left( ∑ _{i = 1} ^{n} \frac{1}{n} x_i \right) \ge ∑ _{i = 1}^{n} \frac{1}{n}\ln (x_i)
$$

$$
∑_{i = 1}^{n} \frac{1}{n} \ln (x_i) = \ln \left( \prod_{i=1}^{n x_i^{1/n}}\right)
$$
D'ou:
$$
\frac{∑_{i = 1}^{n} x_i}{n} \ge \left(\prod_{i=1}^{n x_i}\right)^{1/n}
$$
L'inégalité arithmético-géométrique (gauche = arithmétique, et droite géométrique)
