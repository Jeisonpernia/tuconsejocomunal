# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date

from openerp.osv import fields, osv
from openerp.exceptions import UserError
from openerp import api
from openerp import SUPERUSER_ID, models
import openerp

class partner(osv.osv):
    _name = 'res.partner'
    _inherit="res.partner"

    _columns = {
        'is_persona': fields.boolean('Persona'),
    }


class tcc_personas(osv.osv):
    _name = 'tcc.personas'
    _inherits = {'res.users': 'user_id'}
    _rec_name='name'
    
    
    def group_default(self, cr, uid, ids, context=None):
        dataobj = self.pool.get('ir.model.data')
        result = []
        try:
            dummy,group_id = dataobj.get_object_reference(cr, SUPERUSER_ID, 'base', 'group_user')
            result.append(group_id)
            dummy,group_id = dataobj.get_object_reference(cr, SUPERUSER_ID, 'base', 'group_partner_manager')
            result.append(group_id)
            dummy,group_id = dataobj.get_object_reference(cr, SUPERUSER_ID, 'tcc_noticias', 'group_tcc_residentes')
            result.append(group_id)
        except ValueError:
            # If these groups does not exists anymore
            pass
        return result
    
    _columns={
		'user_id':fields.many2one(
                    'res.users',
                    'Id del usuario del Consejo Comunal',
                    ondelete='cascade',
                    ),
		'consejocomunal_id': fields.many2one(
                    'tcc.consejocomunales',
                    'Consejo Comunal',
                    required=True,
                    ),
        'familia_id': fields.many2one(
                    'tcc_familia.tcc_familia',
                    'Nombre del Grupo Familiar',
                    required=True,
                    ),
		'cedula': fields.integer(
                    'Cédula',
                    size=8,
                    required=True,
                    ),
		's_nombre': fields.char(
                    'Segundo Nombre',
                    ),
		'p_apellido': fields.char(
                    'Primer Apellido',
                    required=True,
                    ),
		's_apellido': fields.char(
                    'Segundo Apellido',
                    ),
		'fecha_nacimiento': fields.date(
                    'Fecha de Nacimiento',
                    required=True,
                    ),
		'estado_civil': fields.selection([
                    ('Soltero','Soltero'),
                    ('Casado','Casado'),
                    ('Divorsiado','Divorsiado')],
                    'Estado Civil',
                    required=True,
                    ),
		'nacionalidad': fields.selection([
                    ('Venezolano','Venezolano'),
                    ('Estranjero','Estranjero')],
                    'Nacionalidad',
                    required=True,
                    ),
		'telefono': fields.char(
                    'Teléfono',
                    required=True,
                    ),
		'sexo': fields.selection(
                    [('masculino','Masculino'),
                    ('femenino','Femenino')],
                    'Sexo',
                    required=True,
                    ),
		'status': fields.selection([('vivo','Con Vida'),('muerto','Fallecido')],'Estado'),
		'active': fields.boolean('Activo',default=True),
        
	}
    #~ email = openerp.fields.Char(related='user_id.login', inherited=True)

    _defaults={
		'is_persona':True,
        'groups_id': group_default,
    }
    
    def create(self, cr, uid, vals, context=None):
        user_id = super(tcc_personas, self).create(cr, uid, vals, context=context)
        user = self.browse(cr, uid, user_id, context=context)
        mail = user.user_id.login
        partner_obj = self.pool['res.partner']
        res_partner_id = partner_obj.search(cr, SUPERUSER_ID, [('id','=',user.user_id.partner_id.id)])
        partner_obj.write(cr, SUPERUSER_ID, res_partner_id, {'email': mail}, context)
        return user_id
