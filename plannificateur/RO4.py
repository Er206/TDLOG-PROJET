import RO3
import data

def planning(firm, nb_packages, nb_articles_package):
    (planning, nb_interim, nb_operator) = RO3.planning(firm, nb_packages, nb_articles_package)
    for i in range(0,data.nb_run_RO):
        (p,i,o) = RO3.planning(firm, nb_packages, nb_articles_package)
        if o < nb_operator :
            (planning, nb_interim, nb_operator) = (p,i,o)
    return (planning, nb_interim, nb_operator)