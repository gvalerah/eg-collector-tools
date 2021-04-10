# =============================================================================
# View Test Progress Bar
# (c) Sertechno 2020
# GLVH @ 2020-03-20
# =============================================================================

from flask import Response

from emtec.collector.forms import frm_test_progress

@main.route('/test_progress',methods=['GET','POST'])
def test_progress():
    data={  'title':'CIs calculados',
        }
    form=frm_test_progress()
    form.Period.choices=[
        (1,"Valor 1"),
        (2,"Valor 2"),
        (3,"Valor 3"),
    ]
    return render_template(
        'test_progress_1.html',
        data=data,
        form=form
        )
     
@main.route('/progress',methods=['GET','POST'])
def progress():
    print("enter progress ...")
    def generate():
        x = 0
        print("enter generate ... x=",x)
        
        while x <= 100:
            print("in loop x=",x)
            yield "data:%s\n\n"%x
            x = x + 10
            time.sleep(1.0)
        print("exit generate ... x=",x)
            
    print("exiting progress ...")
    return Response(
                generate(), 
                mimetype= 'text/event-stream'
                )
