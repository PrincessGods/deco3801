//window width
var winWidth = $( window ).width();
$(".carousel-inner").css("font-size", winWidth/25.6);

var currentStep = $($('#forms').children().get(0));
var currentStepImg = $($('#stepImg').children().get(0));
var currentStepLabel = $($('#topLabels').children().get(0));

function dropControl(){
    if(winWidth < 768){
        document.getElementById("dropdown_menu").style.position = "relative";
    } else{
        document.getElementById("dropdown_menu").style.position = "absolute";
    }

    if(document.getElementById("dropdown_menu").style.height == "82px"){
        document.getElementById("dropdown_menu").style.height = "0px";
    } else{
        document.getElementById("dropdown_menu").style.height = "82px";
    }
}

$(document).ready(function(){
    //resize font size when resolution change
    $(window).resize(function(){
        winWidth = $( window ).width();
        $(".carousel-inner").css("font-size", winWidth/25.6);
    })

    $('#nextStep').click(function(e){
        currentStep.next().show();
        currentStep.hide();
        currentStep = currentStep.next();

        currentStepImg.next().show();
        currentStepImg.hide();
        currentStepImg = currentStepImg.next();

        currentStepLabel.next().show();
        currentStepLabel.hide();
        currentStepLabel = currentStepLabel.next();

        if(currentStep.get(0).id != "form0"){
            $('#prevStep').show();
        }

        if(currentStep.get(0).id == "saveJobBtn"){
            for(var i = 0; i < ($('#forms').children()).length; i++){
                $($('#forms').children().get(i)).show(); 
            }
            
            $('#nextStep').hide();
            $('#saveJobBtn').css("display", "flex");
            $('.stepLable').show();
        }
        
        e.preventDefault();
    })

    $('#prevStep').click(function(e){
        if(currentStep.get(0).id == "saveJobBtn"){
            for(var i = 0; i < ($('#forms').children()).length; i++){
                $($('#forms').children().get(i)).hide(); 
            }
            
            $('#nextStep').show();
            $('.stepLable').hide();
        }

        if(currentStep.prev().get(0).id == "form0"){
            $('#prevStep').hide();
        }
        
        currentStep.prev().show();
        currentStep.hide();
        currentStep = currentStep.prev();

        currentStepImg.prev().show();
        currentStepImg.hide();
        currentStepImg = currentStepImg.prev();

        currentStepLabel.prev().show();
        currentStepLabel.hide();
        currentStepLabel = currentStepLabel.prev();

        e.preventDefault();
    })

    $('#up-pic').click(function(e){
        $('#picture').trigger('click'); 
        e.preventDefault();
    })

    $('#picture').change(function(){
        var oFReader = new FileReader();
        oFReader.readAsDataURL(document.getElementById("picture").files[0]);

        oFReader.onload = function (oFREvent) {
            $('#imgPreview').css("background", "url(" + oFREvent.target.result + ") 50% center/cover");
            //$('#imgPreview').attr('src', oFREvent.target.result).show();
        };

        $('#PreviewModal').modal("show");
    })

    $('#saveimg').click(function(e){
        $('#PreviewModal').modal("hide"); 
        e.preventDefault();
    })
});