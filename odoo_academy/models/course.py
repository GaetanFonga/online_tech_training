# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    level = fields.Selection(string='Level',
                            selection=[('beginner', 'Beginner'),
                                      ('intermediate', 'Intermediate'),
                                      ('advanced', 'Advanced')],
                            copy=False)
    
    active = fields.Boolean(string='Active', default=True)
    
    base_price = fields.Boolean(string='Base Price', default=True)
    
    additional_fee = fields.Float(string='Additional fee', default=10.0)
    
    total_price = fields.Float(string='Total Price', readonly=True)
    
    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0.00:
            raise UserError('Base Price cannot be set as Negative.')
            
        self.total_price = self.base_price + self.additionnal_fee
    
    @api.constrains('additional_fee')
    def _chech_additional_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError('Additional fee cannot be less than 10.00: %s' % record.additional_fee)