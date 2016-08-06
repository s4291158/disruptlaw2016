from model_mommy import mommy

SMALL = 5
MEDIUM = 20
LARGE = 100
PASSWORD = '12345'


def print_log(model):
    model_verbose = model._meta.verbose_name.title()
    print("created {0}: {1}".format(model_verbose, model.id))


def meta_gen_users(model_name, size=SMALL):
    model_set = []
    for _ in range(size):
        model = mommy.make(
            model_name
        )
        model.baseuser.set_password(PASSWORD)
        model.baseuser.save()
        model_set.append(model)

        print_log(model)
    return model_set


def meta_gen(model_name, size=SMALL):
    model_set = []
    for _ in range(size):
        model = mommy.make(
            model_name
        )
        model_set.append(model)
        print_log(model)
    return model_set
