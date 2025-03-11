from django.shortcuts import render,HttpResponse,redirect
from urbanchattelapp.models import Property
# from .filters import PropertyFilter
# Create your views here.


def property_list(request):
    property = Property.objects.all()

    # Manual filters
    name = request.GET.get('name')
    price_max = request.GET.get('price_max')
    price_min = request.GET.get('price_min')
    location = request.GET.get('location')
    builder = request.GET.get('builder')


    if name:
        property = property.filter(name__icontains=name)
    if price_max:
        property = property.filter(price_max=price_max)
    if price_min:
        property = property.filter(price_min=price_min)
    if location:
        property = property.filter(location=location)
    if builder:
        property = property.filter(builder=builder)

    return render(request, 'property_list.html', {'property': property})


def upload_image(request):
    if request.method == 'POST':
        name = request.POST['name']    
        location = request.POST['location']
        price_min = request.POST['price_min']
        price_max = request.POST['price_max']
        project_size_units = request.POST['project_size_units']
        project_size_acres = request.POST['project_size_acres']
        configurations = request.POST['configurations']
        flat_size_min = request.POST['flat_size_min']
        property_type = request.POST['property_type']
        flat_size_max = request.POST["flat_size_max"]
        image = request.FILES['image']
        about = request.POST['about']
        project_status = request.POST["project_status"]
        loaclity = request.POST['loaclity']
        builder = request.POST['builder']
        micro_market = request.POST['micro_market']
        gymnasium = request.POST['gymnasium']
        swimming_pool = request.POST['swimming_pool']
        kids_pool = request.POST['kids_pool']
        badminton_court = request.POST['badminton_court']
        tennis_court = request.POST['tennis_court']
        cricket = request.POST['cricket']
        kid_play_areas = request.POST['kid_play_areas']
        Basketball = request.POST['Basketball']
        Volleyball = request.POST['Volleyball']
        yoga_areas = request.POST['yoga_areas']
        jogging = request.POST['jogging']
        table_tennis = request.POST['table_tennis']
        Power_backup = request.POST['Power_backup']
        treated_water_supply = request.POST['treated_water_supply']
        Guest_house = request.POST['Guest_house']
        water_supply = request.POST['water_supply']
        lift = request.POST['lift']
        party_lawn = request.POST['party_lawn']

        property = Property.objects.create(name=name,location=location,price_min=price_min,price_max=price_max,
            project_size_units=project_size_units,project_size_acres=project_size_acres,configurations=configurations,
            flat_size_min=flat_size_min,flat_size_max=flat_size_max,image=image,property_type=property_type,about=about,
            project_status=project_status, loaclity=loaclity,builder=builder,micro_market=micro_market,gymnasium=gymnasium,swimming_pool=swimming_pool,
            kids_pool=kids_pool,badminton_court=badminton_court,tennis_court=tennis_court,cricket=cricket,kid_play_areas=kid_play_areas,Basketball=Basketball,
            Volleyball=Volleyball,yoga_areas=yoga_areas,jogging=jogging,table_tennis=table_tennis,Power_backup=Power_backup,
            treated_water_supply=treated_water_supply,Guest_house=Guest_house,water_supply=water_supply,lift=lift,party_lawn=party_lawn)
    
        
        return redirect('property_list')
    return render(request,'upload.html')

def property_detail(request, pk):
    property = Property.objects.get(id=pk)
    return render(request, 'property_detail.html', {'property': property})



