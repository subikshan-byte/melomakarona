from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage
from .models import Cart, CartItem, Product, ProductImage

# Helper function to get product data including first image + sizes
def get_product_data1(products):
    product_list = []
    for product in products:
        product_image = ProductImage.objects.filter(p_id=product,priority='first').first()
        image_url = product_image.image.url if (product_image and product_image.image and hasattr(product_image.image, 'url')) else None
        sizes = ""

        product_dict = {
            'p_id': product.p_id,
            'p_name': product.p_name,
            'point1': product.point1,
            'point2': product.point2,
            'brand_name': product.brand_name,
            'desc': product.desc,
            'price': product.price,
            'del_price': product.del_price,
            'category': product.category.c_name,
            'delivery_times': product.delivery_times,
            'save': product.save_upto,   # make sure field name matches your model
            'new': product.new,

            'stock_status': product.stock_status,
            'where': product.where_in_home,
            'where_to_display': product.where_to_display,
            'slug': product.slug,
            'image_url':image_url
            
        }
        product_list.append(product_dict)
    return product_list
def product_detail(request, p):
    # ---------------- SPECIFIC PRODUCT ----------------
    product = get_object_or_404(Product, slug=p)

    # Main product (only one object, so wrap in list and unpack first)
    main_product_data = get_product_data1([product])[0]

    # All images of this product (not just the first one)

    # ---------------- SAME BRAND PRODUCTS ----------------
    same_brand_products = Product.objects.filter(
        brand_name=product.brand_name
    ).exclude(p_id=product.p_id)
    same_brand_data = get_product_data1(same_brand_products)

    # ---------------- SAME CATEGORY PRODUCTS ----------------
    same_category_products = Product.objects.filter(
        category=product.category
    ).exclude(p_id=product.p_id)
    same_category_data = get_product_data1(same_category_products)
    current_url=(request.build_absolute_uri()).replace("190.92.175.39:8000","angels-glamnglow.in")
    product = get_object_or_404(Product, slug=p)
    product_other_image = ProductImage.objects.filter(p_id=product.p_id,priority='No')
    
    # ---------------- CONTEXT ----------------
    products = []
    price=0
    log='0'
    if not request.user.is_authenticated:
        log='1'
    else:
        cart, created = Cart.objects.get_or_create(user=request.user)
        products = CartItem.objects.filter(cart=cart).count
    context = {
        'product': main_product_data,  
          'current_url': current_url,     # dict with all product details
                 # queryset of all images
        "product_other_image":product_other_image,
        'same_brand_products': same_brand_data,
        'same_category_products': same_category_data,
        "cart":products,
        "price":price,
        "log":log,
        "is_logged_in": request.user.is_authenticated,
        "user": request.user if request.user.is_authenticated else None,
    }

    return render(request, 'productdetails-fullwidth.html', context)
def singleproduct(request):
    return render(request,"productdetails-fullwidth.html")