# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date

from openerp.osv import fields, osv
from openerp.exceptions import UserError
from openerp import api
from openerp import SUPERUSER_ID, models

class partner(osv.osv):
    _name = 'res.partner'
    _inherit="res.partner"

    _columns = {
        'is_consejo': fields.boolean(
                    'Consejo Comunal',
                    ),

        'rif': fields.char(
                    'RIF',
                    size=15,
                    required=True,
                    help='R.I.F. del Consejo Comunal'
                    ),
        #~ 'estado_id':fields.many2one(
                    #~ 'res.estados',
                    #~ 'Estado',
                    #~ required=True,
                    #~ ),
        #~ 'municipio_id':fields.many2one(
                    #~ 'res.municipios',
                    #~ 'Municipio',
                    #~ required=True,
                    #~ ),
        #~ 'parroquia_id':fields.many2one(
                    #~ 'res.parroquias',
                    #~ 'Parroquia',
                    #~ required=True
                    #~ ),
    }
    
    
    _sql_constraints = [
        ('rif_key', 'UNIQUE (rif)',  'EL RIF ingresado ya se encuentra registrado, verifique!')
    ]
    
    
class tcc_consejocomunales(osv.osv):
    _name = 'tcc.consejocomunales'
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
            dummy,group_id = dataobj.get_object_reference(cr, SUPERUSER_ID, 'base', 'group_survey_manager')
            result.append(group_id)
            dummy,group_id = dataobj.get_object_reference(cr, SUPERUSER_ID, 'project', 'group_project_manager')
            result.append(group_id)
            dummy,group_id = dataobj.get_object_reference(cr, SUPERUSER_ID, 'tcc_noticias', 'group_tcc_consejo')
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
        'cd_situr':fields.char(
                    'Código SITUR',
                    help='Nombre del Consejo Comunal',
                    ),
        'fecha':fields.date(
                    'Fecha de creación',
                    help='Nombre del Consejo Comunal',
                    ),
        'active':fields.boolean('Activo',
                    help='Si esta activo el motor lo incluiraá en la vista...'),
    }
    
    
    
    _defaults={
        'active':True,
        'is_consejo':True,
        'groups_id': group_default,
    }
    
    _sql_constraints = [
        ('cd_situr_key', 'UNIQUE (cd_situr)',  'EL RIF ingresado ya se encuentra registrado, verifique!')
    ]
    
    def limpiar_campos(self,cr,uid,ids,nombre):
        res_users_obj = self.pool.get('res.users')
        res=res_users_obj.limpiar_campos(cr,uid,ids,nombre)
        return res
    
    def on_change_validate_date(self, cr, uid, ids, fecha, context=None):
        res = {}
        msg = {}
        if fecha:
            if cmp(datetime.strptime(fecha, '%Y-%m-%d').date(), date.today()) == 1:
                msg = {
                    'title':('Error de fecha'),
                    'message':('La fecha seleccionada no puede ser mayor a la fecha de hoy.'),
                        }
                res = {
                    'fecha':'',
                    }
        return {'warning':msg, 'value':res}
    
    def create(self, cr, uid, vals, context=None):
        vals.update({
            'name':vals['name'].upper(),
            })
        user_id = super(tcc_consejocomunales, self).create(cr, uid, vals, context=context)
        user = self.browse(cr, uid, user_id, context=context)
        mail = user.user_id.login
        partner_obj = self.pool['res.partner']
        res_partner_id = partner_obj.search(cr, SUPERUSER_ID, [('id','=',user.user_id.partner_id.id)])
        partner_obj.write(cr, SUPERUSER_ID, res_partner_id, {'email': mail}, context)
        return user_id
        
        
    
    def write(self, cr, uid, ids, vals, context=None):
        if 'name' in vals.keys():
            vals.update({'name':vals['name'].upper(),})
        return super(tcc_consejocomunales, self).write(cr, uid, ids, vals, context=context)

