# Projet pour de session

## Comment utiliser git
**important** il ne faut jamais toucher a la branche main!!
Le développement se fait sur une "feature branch" 
Vous pouvez utiliser ma configuration git [ma config git](https://github.com/eclipxia/dotfiles/blob/main/.gitconfig)
il faut changer le email et le username.
création de clée ssh
```sh
#génaire la clée
ssh-keygen
# voir la clée pour github
cat ~/.ssh/id_ed25519.pub 
```
Aller sur vos paramètre sur github dans la section ssh key. 
Ajouter 1 clée de sining et 1 clée de auth.

| alias | function | description |
| --- | --- | --- |
| wc | worktree | Clone en initialisant un work tree |
| wnew | worktree | Crée une nouvelle branche en worktree |
| wd | worktree | Delete la branche et delete la directory (local) |
| c | commit | Commit verbose et push (sined) |
| a | add | Run add |
| ap | add | Demmande se que tu veux add | 

Chaque fois que tu veux travailler sur une feature vas dans main et `git pull
upstream main`. 

### Exemple d'utilisation 

```sh
# Cloner le projet
git wc <git@github.com/nom-de-la-repo>
cd <nom-de-la-repo/main>
#Création de la branche de développement
git wnew <nom-de-la-branche>
```

