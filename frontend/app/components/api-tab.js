import Ember from 'ember';

export default Ember.Component.extend({
  didRender() {
    this._super(...arguments);
    $(".moderatorHolder").hide();
  }
});
