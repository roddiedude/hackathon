from complaint.models import Complaint
from category.models import Category
from location.models import Location
import complaint.models
from django.db.models.signals import post_syncdb
from django.contrib.auth.models import User
from django.utils import timezone

def create_complaint(title, description, phone, email, category, locality, photo, username):
    try:
        c = Complaint.objects.get(title__exact=title)
    except Complaint.DoesNotExist:        
        try:
            location = Location.objects.get(name__exact=locality)
            category = Category.objects.get(name__exact=category)
            u = User.objects.get(username__exact=username)        
            
            c = Complaint(user=u)
            c.title = title
            c.information = description
            c.category = category
            c.locality = location
            c.address = ""
            c.date_entered = timezone.now()
            c.photo = photo
            c.email = email        
            
            c.save()
            
        except Location.DoesNotExist:
            print "error"

def my_callback(sender, **kwargs):
    create_complaint(title="Low voltage", 
                     description="There are significant low voltage issues after 6 PM. This causes damages to the appliances.", 
                     phone="429-213-7657", 
                     email="lobortis.risus@non.com", 
                     category="Electrical", 
                     locality="Adyar", 
                     photo="", 
                     username="priyas")
     
    create_complaint(title="Cracks in Bridge", 
                     description="There are major cracks in the pillars on the bridge at Royapuram.", 
                     phone="106-542-5655", 
                     email="ac.fermentum@acmattisornare.edu", 
                     category="Bridges", 
                     locality="Basin Bridge", 
                     photo="", 
                     username="nages")
     
    create_complaint(title="Potholes in roads", 
                     description="There are major potholes in the KK Road in our area leading to difficultdirrving conditions.", 
                     phone="866-828-5020", 
                     email="mollis.lectus@neceleifend.org", 
                     category="Road", 
                     locality="Ice House", 
                     photo="http://www.thehindu.com/multimedia/dynamic/00825/02IN_BAD_ROAD_VYASA_825076g.jpg", 
                     username="karthikeyan")
   
    create_complaint(title="Primary school - no teachers", 
                     description="The primary school in Kamaraj nagar do not have sufficient teachers and most teachers do not come on time.", 
                     phone="555-726-3011", 
                     email="tortor.Nunc@Proinultrices.org", 
                     category="Education", 
                     locality="Kodambakkam", 
                     photo="", 
                     username="iswaryar")
     
    create_complaint(title="No road laid", 
                     description="The road in Emg nagar has not been laid for the last 5 years.", 
                     phone="239-434-9576", 
                     email="viverra@semconsequatnec.edu", 
                     category="Road", 
                     locality="Tondiarpet", 
                     photo="http://newindianexpress.com/cities/chennai/article315735.ece/alternates/w460/1-CBI.jpg", 
                     username="deepanm")
     
    create_complaint(title="Bad roads", 
                     description="the roads in SV colong are very bad and have many potholes.", 
                     phone="388-637-0626", 
                     email="imperdiet@Crasloremlorem.edu", 
                     category="Road", 
                     locality="Pulianthope", 
                     photo="http://www.thehindu.com/multimedia/dynamic/01370/TH-BAD_ROAD__1370040f.jpg", 
                     username="vgp")                       
 
    create_complaint(title="Transformer problem", 
                     description="The transformer in our area runs into heating and burning out problems often and no proper action has been taken.", 
                     phone="599-169-6876", 
                     email="at.sem.molestie@maurissapien.edu", 
                     category="Electrical", 
                     locality="Pulianthope", 
                     photo="", 
                     username="vgp")      
     
    create_complaint(title="Chain snatching", 
                     description="There have been multiple incidences of chain snatching in our area. Even after repeated compliants to the police station, no action has been taken.", 
                     phone="802-556-2785", 
                     email="nec.tempus@eutelluseu.net", 
                     category="Law & Order", 
                     locality="Tondiarpet", 
                     photo="", 
                     username="priyas")
     
    create_complaint(title="Lack of traffic signals", 
                     description="The traffic light at the besant nagar beack junction has not been functioning and results in haphazard traffic conditions.", 
                     phone="907-576-8793", 
                     email="laoreet.posuere.enim@Aliquamgravidamauris.ca", 
                     category="Traffic", 
                     locality="Pulianthope", 
                     photo="http://www.thehindu.com/multimedia/dynamic/00294/HY23TRAFFIC_SIGNAL_294666e.jpg", 
                     username="iswaryar")
     
    create_complaint(title="Mosquitos breeding", 
                     description="There is water stagnation in our area during the rainy season and it becomes a breeding ground for mosquitoes. Recently there were 2 cases on Dengue in our area. This needs to be addressed immediately.", 
                     phone="485-771-4266", 
                     email="nibh@Integerinmagna.net  ", 
                     category="Health", 
                     locality="Tondiarpet", 
                     photo="http://www.thehindu.com/multimedia/dynamic/01250/28TH_MOSQUITO_1250313e.jpg", 
                     username="vgp")
  
    create_complaint("Sewage mixed with metro water", 
                     "There is sewage mixing with metro water in our area very frequently.",
                     "946-539-3269",
                     "Ut@liberoettristique.edu",
                     "Metro Water",
                     "Adyar",
                     "",
                     "priyas")
     
    create_complaint("Congested roads", 
                     "The  VOC nagar has seen significant rise if roadside encroachments that has narrowed down the usable road leading to traffic congestion.",
                     "934-424-3095",
                     "hendrerit.Donec@hymenaeos.net",
                     "Traffic",
                     "Saidapet",
                     "http://walkabilityasia.files.wordpress.com/2012/10/09th_eviction_1231933f.jpg",
                     "deepanm")
                        
    create_complaint("Lack of public toilets", 
                     "There are no public toilets in our area and most people defecate in the public leading to health issues.",
                     "767-779-6712",
                     "cursus.a.enim@Curabitursed.co.uk",
                     "Health",
                     "Nungambakkam",
                     "",
                     "karthikeyan")
     
    create_complaint("Unscheduled power cuts", 
                     "There are unscheduled power cuts ranging from 2 - 4 hours at erratic times put burden on the people.",
                     "894-784-0295",
                     "commodo.ipsum@molestiesodalesMauris.co.uk",
                     "Electrical",
                     "Ice House",
                     "",
                     "karthikeyan")
    
    create_complaint("No Parking available", 
                     "There is no parking available on the FB road.",
                     "126-412-2017",
                     "auctor.ullamcorper.nisl@hendreritconsectetuercursus.org",
                     "Traffic",
                     "Kilpauk",
                     "",
                     "nages")
    
    create_complaint("Garbage dumping", 
                     "The street end of MRC nagar has unscruplous duping of wate. There is no proper grabage bin placed by the corporation for the residents of this area.",
                     "500-469-0514",
                     "id@nullaat.net",
                     "Solid Waste Management",
                     "Ayanavaram",
                     "http://www.thehindu.com/multimedia/dynamic/00748/garbage_748122f.jpg",
                     "nages")
                    
    create_complaint("Littering and dumping", 
                     "The open area near our colony is used by the nearby industries as a garbage dumping yard and should be stopped.",
                     "688-109-5391",
                     "augue.eu@velit.net",
                     "Solid Waste Management",
                     "Kodambakkam",
                     "http://www.thehindu.com/multimedia/dynamic/01541/Garbage_1541798f.jpg",
                     "nages")

    create_complaint("Sound nuisance", 
                     "The temple near our area uses conical loud speakers to air songs etc. This causes public nuisance. On approching the temple autorities to remove this has yielded no cooperation from them and they are threatnening us with dire consequences in this is made an issue. Please help.",
                     "361-814-0449",
                     "morbi.tristique.senectus@inmolestietortor.co.uk",
                     "Law & Order",
                     "Nungambakkam",
                     "",
                     "priyas")
    
    create_complaint("Damaged roads", 
                     "The roads in my locality SV nagar are damaged badly after the rains.",
                     "934-424-3078",
                     "ut.dink@hendrerit.edu",
                     "Road",
                     "Saidapet",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcR58EaD_-s5MfnLDRwPpAjVLtiUp65sp2vtEo6b5bEncWwjbZJW",
                     "vgp")
    
    create_complaint("Multiple potholes in roads", 
                     "There are may potholes in the roads in my area since the last 8 months.",
                     "275-102-7506",
                     "et@nislarcu.ca",
                     "Road",
                     "Adyar",
                     "http://www.hindu.com/2009/11/17/images/2009111750080201.jpg",
                     "iswaryar")
    
    create_complaint("Narrow roads", 
                     "The roads leading from Kb nagar to MM colong are very narrow that allows safe passage of only one car at a time. This eneds to be widened.",
                     "239-434-9576",
                     "viverra@semconsequatnec.edu",
                     "Road",
                     "Adyar",
                     "http://www.thehindu.com/multimedia/dynamic/00662/18HYDPS04-NZB2_GHG2_662161f.jpg",
                     "iswaryar")
    
    create_complaint("No trees on the roads", 
                     "The SH42 has no trees on the roadside as many of them have been cut recently. The road side should be re-planted with the trees.",
                     "275-102-7506",
                     "et@nislarcu.ca",
                     "Road",
                     "Ayanavaram",
                     "",
                     "iswaryar")    
   
                        
# Live wire    There was a live wire on the road and has not been attended to by the TNEB even after repeated calls to them.    568-817-0456    Mauris@ultricessit.org    Electrical    Ice House    
# PHC lacking doctors    The public health center in our area is lacking doctors and patients do not get proper care.    275-102-7506    et@nislarcu.ca    Health    Adyar    
# Narrow Bridge    The bridge in jeeva nagar is very narrow causing congestion and traffic issues    679-707-1047    ut.eros@hendrerit.edu    Bridges    Tondiarpet    
# Median damaged in Bridge    The median in the Nungambakkam gemini flyover is damaged and the stones are strewn on the road    855-235-2230    Nunc@egestas.net    Bridges    Kilpauk    
                        

     
# Waterlogging on roads    The road in my area is prone to waterlogging because it has not been designed properly.    866-828-5020    mollis.lectus@neceleifend.org    Road    Adyar    http://www.thehindu.com/multimedia/dynamic/00300/03THARUMBAKKAM_300925f.jpg
# Potholes in roads    There are major potholes in the KK Road in our area leading to difficultdirrving conditions.    239-434-9576    viverra@semconsequatnec.edu    Road    Adyar    http://www.thehindu.com/multimedia/dynamic/01431/TH17_CTH_ROAD_1431456f.jpg
                    

    
    
    
    
    
post_syncdb.connect(my_callback, sender= complaint.models)