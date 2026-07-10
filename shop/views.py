from django.shortcuts import  redirect , get_object_or_404
from django.views.generic import ListView ,CreateView , FormView  , View , DetailView , TemplateView
from .models import Product , Signup , Like , Comment
from .forms import  LoginForm , SignupForm
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password, check_password #Hashing and checking passwords


# Create your views here.
'''
This view displays all products stored in the database using Django's ListView.
The products are rendered in the "home.html" template, and the context object
name is set to "products" so they can be accessed easily in the template.
If a user_id exists in the session, the corresponding user object is added
to the template context.
'''

#listview in home 
class HomePageListView(ListView):
    model = Product            
    template_name = "home.html"
    context_object_name = "products"    
    # check if user is logged in and add user to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_id = self.request.session.get("user_id")

        if user_id:
            try:
                context["user"] = Signup.objects.get(id=user_id)
            except Signup.DoesNotExist:
                context["user"] = None
        else:
            context["user"] = None

        return context
#signup view
class SignupPageView(CreateView):
    model = Signup
    form_class =SignupForm
    template_name = "signup.html"
    # form_valid method is overridden to hash the password before saving the user object to the database.
    def form_valid(self, form):
        user = form.save(commit=False)

        user.password = make_password(user.password)

        user.save()
        self.request.session["user_id"] = user.id
        self.request.session["user_name"] = user.name
        

        return redirect("home")


#login
class LoginPageView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    # form_valid method is overridden to check the user's credentials and log them in if they are valid.
    def form_valid(self, form):
        phone = form.cleaned_data["phone"]
        password = form.cleaned_data["password"]

        if not Signup.objects.filter(phone=phone).exists():
            form.add_error("phone", "Phone number does not exist.")
            return self.form_invalid(form)

        user = Signup.objects.get(phone=phone)

        if not check_password(password, user.password):
            form.add_error("password", "Incorrect password.")
            return self.form_invalid(form)
        self.request.session["user_id"] = user.id
        self.request.session["user_name"] = user.name
        return redirect("home")
#logout 
class LogoutPageView(View):
    def get(self, request):
        request.session.flush()   # Clear the session
        return redirect("home")
    

#DetailView
class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


#CartView
from django.shortcuts import redirect
from django.views.generic import TemplateView


class CartView(TemplateView):
    template_name = "cart.html"
    '''def dispatch method is overridden to check if the user is logged
            in before allowing access to the cart page. If the user is not logged
                in, they are redirected to the signup page.'''
    def dispatch(self, request, *args, **kwargs):
        user_id = request.session.get("user_id")

        if not user_id:
            return redirect("signup")

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = self.request.session.get("cart", {})

        products = []
        total = 0

        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)

            subtotal = product.price * quantity
            total += subtotal

            products.append({
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal,
            })

        context["products"] = products
        context["total"] = total

        return context
#AddToCartView  
class AddToCartView(View):
 
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        cart = request.session.get("cart", {})
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("signup")


        if str(product.id) in cart:
            cart[str(product.id)] += 1
        else:
            cart[str(product.id)] = 1

        request.session["cart"] = cart

        return redirect("home")
#Remove View  
class RemoveFromCartView(View):

    def post(self, request, pk):
        cart = request.session.get("cart", {})

        product_id = str(pk)

        if product_id in cart:
            if cart[product_id] > 1:
                cart[product_id] -= 1
            else:
                del cart[product_id]

        request.session["cart"] = cart

        return redirect("cart")
#Like Views   
class LikeProductView(View):

    def post(self, request, pk):

        user_id = request.session.get("user_id")

        if not user_id:
            return redirect("signup")


        user = Signup.objects.get(id=user_id)

        product = get_object_or_404(
            Product,
            id=pk
        )


        like, created = Like.objects.get_or_create(
            user=user,
            product=product
        )


        if not created:
            like.delete()


        return redirect("home")
#Mylike View
class MyLikesView(ListView):
    template_name = "likes.html"
    context_object_name = "products"

    def dispatch(self, request, *args, **kwargs):
        user_id = request.session.get("user_id")

        if not user_id:
            return redirect("signup")

        return super().dispatch(request, *args, **kwargs)


    def get_queryset(self):

        user_id = self.request.session.get("user_id")

        user = Signup.objects.get(id=user_id)

        likes = Like.objects.filter(
            user=user
        )

        return Product.objects.filter(
            like__in=likes
        )
#add comment view   
class AddCommentView(View):

    def post(self, request, pk):

        user_id = request.session.get("user_id")

        if not user_id:
            return redirect("signup")

        #Finds the user from the database.
        user = Signup.objects.get(id=user_id)

        product = get_object_or_404(
            Product,
            id=pk
        )

        text = request.POST.get("text")

        if text:

            Comment.objects.create(
                user=user,
                product=product,
                text=text
            )

        return redirect(
            "product_detail",
            pk=pk
        )
#Profile Views
class ProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_id = self.request.session.get("user_id")

        if user_id:
            try:
                context["user"] = Signup.objects.get(id=user_id)
            except Signup.DoesNotExist:
                context["user"] = None
        else:
            context["user"] = None

        return context

#search view
class SearchResultsView(ListView):
    model = Product
    template_name = "search_results.html"
    context_object_name = "products"
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Product.objects.filter(name__icontains=query)