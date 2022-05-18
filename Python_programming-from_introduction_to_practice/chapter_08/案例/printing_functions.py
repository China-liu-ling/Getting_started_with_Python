def print_and_transfer(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_complete(completed_models):
    print("\nThe following models have been printed: ")
    for complete_model in completed_models:
        print(f"-{complete_model}")