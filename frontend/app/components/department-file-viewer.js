import Ember from 'ember';


export default Ember.Component.extend({
   actions: {
    moreInfo(){
        for(var i = 0; i <= Ember.$(".document").length; i++){
          if(Ember.$(".more-info-button").index(event.target) === i){
           Ember.$( ".document:eq("+i+")" ).removeClass( "document-view-document" );
           Ember.$( ".document:eq("+i+")" ).toggleClass( "document-more-info" );
           Ember.$( ".view-document:eq("+i+")" ).hide();
           Ember.$( ".more-info:eq("+i+")" ).toggle("fast");
            }
        }

      },
      viewDocument(){
        for(var i = 0; i <= Ember.$(".document").length; i++){
          if(Ember.$(".view-document-button").index(event.target) === i){
           Ember.$( ".document:eq("+i+")" ).removeClass( "document-more-info"  );
           Ember.$( ".document:eq("+i+")" ).toggleClass( "document-view-document" );
           Ember.$(".more-info:eq("+i+")").hide();
           Ember.$(".view-document:eq("+i+")").toggle("fast");
            }
        }
      },
      setDocumentStatus(status , color, buttonType, name){
        var thisParents = Ember.$(event.target).parents().eq(6);
        var thisParentSiblings = Ember.$(event.target).parent().siblings();
        thisParents.data('item', status);
        thisParents.attr('data-item', status);
        thisParents.css("border-left", "5px solid "+color+"");
        thisParentSiblings.text(Ember.$(event.target).text());
        thisParentSiblings.removeClass( );
        thisParentSiblings.toggleClass( buttonType);
        if(Ember.$(".active").data("filter") !== ".read, .unread, .archived"){
          if(Ember.$(".active").data("filter") !== status){
            Ember.$(event.target).parents().eq(6).hide("slide");
            Ember.$.bootstrapGrowl("Successfully changed document status to " + Ember.$(event.target).text() + "!", { type: 'success', align: 'center' , width: 400, hight: 40 });
          }
        }
        else{
        Ember.$.bootstrapGrowl("Successfully changed document status to " + Ember.$(event.target).text() + "!", { type: 'success', align: 'center' , width: 400, hight: 40 });
        }

        console.log("update database to archive");

    }
   }
});

