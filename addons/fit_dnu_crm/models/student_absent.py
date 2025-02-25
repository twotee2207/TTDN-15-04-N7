from odoo import models, fields, api


class StudentAbsent(models.Model):
    _name = 'student_absent'
    _description = 'Quản lý sinh viên vắng'
    _rec_name = 'student_id'

    # display_name = fields.Char(
    #                     compute = "_compute_display_name",
    #                     store = True
    #                 )
    student_id = fields.Many2one("student", string = "Sinh viên", ondelete = 'cascade', required = True)
    student_code = fields.Char(related = 'student_id.student_code', string = "Mã sinh viên")
    full_name = fields.Char(related = 'student_id.full_name', string = "Họ tên")
    student_class_id = fields.Many2one(
                comodel_name='student_class',
                related = "student_id.student_class_id", 
                string = "Lớp",
                store = True,
                )
    student_cohort_id = fields.Many2one(
                comodel_name='student_cohort',
                related = "student_id.student_cohort_id", 
                string = "Khóa",
                store = True,
                )
    # date_id = fields.Many2one("date_manager", 
    #                         string = "Ngày",
    #                         compute = "_compute_date_id",
    #                         store = True,
    #                         )
    student_class_absent_id = fields.Many2one("student_class_absent", 
                            string = "Lớp - SV vắng",
                            compute = "_compute_student_class_absent_id",
                            store = True,
                        )
    date_absent = fields.Date("Ngày vắng", required = True)
    reason = fields.Char("Lý do")
    day = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
    ], string='Ngày', compute = "_compute_day_month_year", store = True)

    month = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ], string='Tháng', compute = "_compute_day_month_year", store = True)

    year = fields.Selection([
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
        ('2031', '2031'),
        ('2032', '2032'),
        ('2033', '2033'),
        ('2034', '2034'),
    ], string='Năm', compute = "_compute_day_month_year", store = True)

    _sql_constraints = [
        ('student_day_absent_uniq', 'unique(student_id, date_absent)', 'Đã tồn tại bản ghi sinh viên với ngày vắng này'),
    ]


    @api.depends(
        "date_absent",
    )
    def _compute_day_month_year(self):
        for record in self:
            if record.date_absent:
                record.day = str(record.date_absent.day)
                record.month = str(record.date_absent.month)
                record.year = str(record.date_absent.year)

    # @api.depends(
    #     "date_absent",
    # )
    # def _compute_date_id(self):
    #     for record in self:
    #         if record.date_absent:
    #             date = self.env["date_manager"].search([
    #                 ('date','=', record.date_absent)
    #             ])
    #             if len(date) > 0:
    #                 record.date_id = date.id
    #             else:
    #                 date_cre = self.env["date_manager"].create({
    #                     'date': record.date_absent
    #                 })
    #                 record.date_id = date_cre.id
    
    @api.depends(
        "date_absent",
        "student_id",
        "student_class_id"
    )
    def _compute_student_class_absent_id(self):
        for record in self:
            if record.date_absent and record.student_id and record.student_class_id:
                stu_class_abs = self.env["student_class_absent"].search([
                    ('date_absent','=', record.date_absent),
                    ('student_class_id', '=', record.student_class_id.id)
                ])
                if len(stu_class_abs) > 0:
                    record.student_class_absent_id = stu_class_abs.id
                else:
                    data_cre = self.env["student_class_absent"].create({
                        'date_absent': record.date_absent,
                        'student_class_id': record.student_class_id.id
                    })
                    record.student_class_absent_id = data_cre.id