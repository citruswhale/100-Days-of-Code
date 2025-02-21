La plupart des IDE (Environnements de Développement Intelligent) tels que PyCharm disposent d'outils intégrés pour le débogage. Cela est généralement connu sous le nom de débogueur. De nombreuses façons, ils sont comme des instructions d'impression sur les stéroïdes.

Les débogueurs nous permettent de regarder dans notre code pendant l'exécution et de faire une pause sur les lignes choisies pour comprendre quel est le mécanisme interne et où cela se passe mal.

Il y a quelques choses qui sont les mêmes dans la plupart des IDE avec lesquelles vous devriez être familier :

1. **Point d'arrêt** - Vous pouvez définir un point d'arrêt en cliquant sur une ligne dans la marge du code (où se trouvent les numéros de ligne). Cette ligne sera l'endroit où le programme se met en pause pendant l'exécution du débogage.

2. **Pas à Pas** - Ce bouton parcourra l'exécution de votre code ligne par ligne et vous permettra de voir les valeurs intermédiaires de vos variables.
3. **Entrer dans** - Cela entrera dans tous les autres modules que votre code référence. Par exemple, si vous utilisez une fonction du module aléatoire, il vous montrera le code original de cette fonction afin que vous puissiez mieux comprendre sa fonctionnalité et comment elle se rapporte à vos problèmes.
4. **Entrer dans Mon Code** - Cela fait la même chose que Entrer dans, mais limite la portée à votre propre code de projet et ignore le code de la bibliothèque comme aléatoire.

### PAUSE 1
Utilisez le débogueur de PyCharm pour comprendre quel est le problème dans le code de départ et corrigez-le.