def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total = 0 
    return {"total_carrito": total}
    '''(int(value["acumulado"])) '''