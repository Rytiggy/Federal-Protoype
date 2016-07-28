import Ember from 'ember';

export default Ember.Route.extend({
 beforeModel: function() {
    if(document.location.pathname === "/researcher/grant"){ this.transitionTo('researcher.grant'); }
    else if(document.location.pathname === "/researcher/metadata"){ this.transitionTo('researcher.metadata'); }
    else{this.transitionTo('researcher.grant'); }
  },
  model() {
      return Ember.RSVP.hash({
      departments: this.store.findAll('department'),
      document: this.store.createRecord('document'),
      grant: this.store.createRecord('grant'),
    });
    },
});
